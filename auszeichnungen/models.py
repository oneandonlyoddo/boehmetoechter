# -*- coding: utf8 -*- 
from django.db import models
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


class Veranstalter(models.Model):
	name = models.CharField(max_length=2000,verbose_name='Beschreibung oder Titel der Auszeichnung')
	jahr = models.CharField(verbose_name='Jahr der Auszeichnung', max_length=4)
	def __unicode__(self):  # Python 3: def __str__(self):
		return u'%s, %s' % (self.name, self.jahr)
	class Meta:
		verbose_name_plural = "Veranstalter"

class Auszeichnung(models.Model):
	titel = models.CharField(verbose_name='z.B. Gold oder bester Wein', max_length=255)
	veranstalter = models.ForeignKey('auszeichnungen.Veranstalter')
	def __unicode__(self):  # Python 3: def __str__(self):
		return u'%s %s' % (self.veranstalter, self.titel)
	class Meta:
		verbose_name_plural = "Auszeichnungen"

class AuszeichnungsForm(ModelForm):

    class Meta:
        model = Auszeichnung
        fields = ['titel','veranstalter']

class AuszeichnungsPlugin(CMSPlugin):
    auszeichnung = models.ForeignKey('auszeichnungen.Auszeichnung', related_name='plugins')

    def __unicode__(self):
      return self.auszeichnung.titel
       
        