# -*- coding: utf-8 -*-
"""
Holds all the information relevant to the client (addresses for instance)
"""
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _




BASE_ADDRESS_TEMPLATE = \
_("""
Name: %(name)s,
Addresse: %(address)s,
PLZ: %(zipcode)s,
Stadt: %(stadt)s,
Land: %(land)s,
Email: %(email)s,
Telefon: %(tel)s,
Fax: %(fax)s,
""")

ADDRESS_TEMPLATE = getattr(settings, 'SHOP_ADDRESS_TEMPLATE',
                           BASE_ADDRESS_TEMPLATE)
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta(object):
        verbose_name = _('Land')
        verbose_name_plural = _('Laender')


class Address(models.Model):
    user_shipping = models.OneToOneField(USER_MODEL, related_name='shipping_address',blank=True, null=True)
    user_billing = models.OneToOneField(USER_MODEL, related_name='billing_address',blank=True, null=True)

    vorname = models.CharField(_('Vorname'), max_length=255)
    nachname = models.CharField(_('Nachname'), max_length=255)
    street = models.CharField(_('Strasse'), max_length=255)
    nr = models.CharField(_('Nr.'), max_length=255, blank=True)
    zip_code = models.CharField(_('Postleitzahl'), max_length=20)
    stadt = models.CharField(_('Stadt'), max_length=20)
    land = models.CharField(_('Land'), max_length=255)
    email = models.CharField(_('Emailadresse'), max_length=255)
    tel = models.CharField(_('Telefon'), max_length=255, blank=True)
    fax = models.CharField(_('Telefax'), max_length=255, blank=True)
    seperateBilling = models.BooleanField()
   

    class Meta(object):
        verbose_name_plural = _("Addressen")
        verbose_name = _('Addresse')

    def __unicode__(self):
        return '%s %s (%s, %s)' % (self.vorname, self.nachname, self.zip_code, self.stadt)

    def clone(self):
        new_kwargs = dict([(fld.name, getattr(self, fld.name))
                           for fld in self._meta.fields if fld.name != 'id'])
        return self.__class__.objects.create(**new_kwargs)

    def as_text(self):
        return ADDRESS_TEMPLATE % {
            'name': '%s %s' % (self.vorname, self.nachname),
            'address': '%s %s' % (self.street, self.nr),
            'zipcode': self.zip_code,
            'stadt': self.stadt,
            'land': self.land,
            'email': self.email,
            'tel': self.tel,
            'fax': self.fax,
            
        }

