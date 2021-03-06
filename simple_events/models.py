# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.template.defaultfilters import date as datefilter
from django.conf import settings
from django.utils.translation import ugettext as _

from cms.models import CMSPlugin # django-cms
from cms.models.fields import PlaceholderField

from hvad.models import TranslatableModel, TranslatedFields
from hvad.manager import TranslationManager


class EventCategory(TranslatableModel):
    on_site = CurrentSiteManager(field_name='sites')
    translations = TranslatedFields(
        name = models.CharField(_(u"Name"), max_length=100)
    )
    slug = models.SlugField(_('Slug'),
            help_text=_('Name in lowercase with no spaces which will be chown in the URL of the navigator'))
    sites = models.ManyToManyField(Site)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    
    objects = TranslationManager()
    
    def site_list(self):
        return self.sites.all()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = _(u'Termin Kategorien')
        verbose_name = _(u'Termin Kategorie')
        

class EventManager(CurrentSiteManager):	

    def upcoming(self, days=None):
        """
        Returns all Events with a start date in the next ``days`` days.
        If ``days`` is None, get all upcoming events.
        Resulting QuerySet is ordered with the soonest event first.
		"""
        now = date.today()
        if days is None:
            return self.get_query_set().filter(
                ((models.Q(end__isnull=True) | models.Q(end__gte=now)) & models.Q(start__gte=now)) |
                (models.Q(start__lte=now) & models.Q(end__gte=now))
            ).order_by('start')
        else:
            return self.get_query_set().filter(
                (models.Q(end__isnull=True) & models.Q(start__range=(now, now + timedelta(days=int(days))))) |
                (models.Q(end__isnull=False) & models.Q(start__range=(now, now + timedelta(days=int(days)))) & models.Q(end__gte=now))
            ).order_by('start')

    def past(self):
        """
        Gets all the Events that have passed.
        Queryset is ordered with the most recently past event first.
        """
        now = date.today()
        return self.get_query_set().filter(models.Q(end__lt=now) | models.Q(end__isnull=True), start__lt=now)

def format(d):
    if d.year == date.today().year:
        s = "F j"
    else:
        s = "F j, Y"
    return mark_safe(datefilter(d, s))

def isValidEndDate(field_data, all_data):
    " Validates that end date is less than (after) the start date. "
    if field_data:
        if  date(*[int(v) for v in field_data.split('-')]) <=  date(*[int(v) for v in all_data['start'].split('-')]):
            raise ValidationError(_("Das Ende des Termins muss nach dem Start stattfinden. Wähle bitte ein anderes Enddatum, oder lasse das Feld frei wenn der Termin nur an einem Tag stattfindet."))

class Event(TranslatableModel):
    img = models.ImageField(verbose_name='Event Bild',upload_to='eventbilder',blank=True, null=True, help_text=_(u'* Optional. Veranstaltungsposter oder ähnliches.'))
    on_site = EventManager(field_name='sites')
    translations = TranslatedFields(
        name = models.CharField(_("Terminname"), max_length=250, 
                help_text=_(u'Zum Beispiel: "Drittes Sommerfest"'))
    )
    location = models.CharField(_("Ort"), max_length=250, blank=True, null=True,
                help_text=_(u'* Optional. Örtlichkeit der Veranstaltung'))
    slug = models.SlugField(_('Kurzname'), unique_for_date='start', 
            help_text=_('Name in Kleinbuchstaben ohne Leerzeichen der in der URL verwendet wird.'))
    description = PlaceholderField('event_description', blank=True, null=True, verbose_name=_('Beschreibung'),)

    start = models.DateField(_(u"Datum"),
        help_text=_(u'Format: jjjj-mm-tt. Wann findet der Termin statt? Wenn der Termin über mehrere Tage stattfindet dann gib ein Startdatum und unten ein Enddatum an.'))
    time = models.CharField(_("Zeitpunkt"), blank=True, max_length=100, 
        help_text=_(u'* Optional.  zum Beispiel: "8", "7 - 8" oder "7:30" das "Uhr" wird automatisch hinzugefügt'))
    # Todo -- continue to validate that the end is after the start?
    end = models.DateField(_(u'Enddatum'), blank=True, null=True,
        help_text=_(u'* Optional.  Wenn der Termin über mehrere Tage andauert dann gebe hier ein Enddatum an. Wenn freigelassen wird automatisch das Startdatum eingetragen.'))
    categories = models.ManyToManyField(EventCategory, blank=True, 
        null=True, limit_choices_to={'sites__id': settings.SITE_ID})
    sites = models.ManyToManyField(Site, editable=False, 
        default=[settings.SITE_ID])
       
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    

    objects = TranslationManager()
    
    def __unicode__(self):
        return self.name
        #return self.description

    @models.permalink
    def get_absolute_url(self):
        return ('event_detail', None, {
            'year': self.start.strftime("%Y"),
            'month': self.start.strftime("%m"),
            'day': self.start.strftime("%d"),
            'slug': self.slug,
            })
        
    def has_passed(self):
        if self.end:
            return self.end < date.today()
        else:
            return self.start < date.today()

    def category_list(self):
        if self.categories.all():
            return ", ".join([ c.name for c in self.categories.all() ])
        return _(u'(No categories)')

    def site_list(self):
        return self.sites.all()

    def is_mutiple_days(self):
        return self.end is not None and self.end > self.start

    def get_next_upcoming(self):
        try:
            return Event.on_site.upcoming().filter(start__gte=self.start).exclude(id=self.id)[0]
        except IndexError:
            return None

    def get_previous_upcoming(self):
        try:
            return Event.on_site.upcoming().filter(start__lte=self.start).exclude(id=self.id)[0]
        except IndexError:
            return None

    def date_span(self):
        if self.end:
            s = "%s &mdash; %s" % (format(self.start), format(self.end))
        else:
            s = format(self.start)
        return mark_safe(s)
    date_span.short_description = 'date'
    date_span.admin_order_field = 'start'
    date_span.allow_tags = True
    
    class Meta:
        ordering = ('-start',)
        verbose_name = _(u'Termin')
        verbose_name_plural = _(u'Termine')
