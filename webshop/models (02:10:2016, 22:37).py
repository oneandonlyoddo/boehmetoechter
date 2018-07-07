# -*- coding: utf8 -*- 
#from shop.models import Product
#from shop_categories.models.defaults.product.base import CategoryProductBase
from shop.models_bases import BaseOrder, BaseProduct
from shop.models_bases.managers import OrderManager
from django import forms




from django.db import models
from django.forms import ModelForm, Textarea

LAGEN_AUSWAHL = (
    ('FE', 'Freyburger Edelacker'),
    ('FM', 'Freyburger Mühlberg'),
    ('FS', 'Freyburger Schweigenberg'),
    ('DR', 'Dorndorfer Rappental'),
    ('OF', 'Ortslage Freyburg'),
    ('OL', 'Ortslage Laucha'),
    ('GB', 'Großjenaer Blütengrund')
)

class LageKategorie(models.Model):
	name = models.CharField(max_length=255,verbose_name='Name')
	slug = models.SlugField(max_length=255,verbose_name='Slug')
	sortID = models.IntegerField(max_length=1,verbose_name='Sortier Position')
	beschreibung = models.CharField(max_length=2000,verbose_name='Beschreibung',blank=True, null=True)
	
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['sortID']
		verbose_name_plural = 'Kategorien'
		verbose_name = 'Kategorie'
        

class LagenKatForm(forms.ModelForm):

    beschreibung = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = LageKategorie

class ArtKategorie(models.Model):
	name = models.CharField(max_length=255,verbose_name='Name')
	slug = models.SlugField(max_length=255,verbose_name='Slug')
	sortID = models.IntegerField(max_length=1,verbose_name='Sortier Position')
	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['sortID']
		verbose_name_plural = 'Weinarten'
		verbose_name = 'Weinart'
        


class ArtKatForm(forms.ModelForm):

    #beschreibung = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = ArtKategorie

class GeschmacksrichtungKategorie(models.Model):
	name = models.CharField(max_length=255,verbose_name='Geschmack')

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Geschmacksrichtungen'
		verbose_name = 'Geschmacksrichtung'
        
class GeschmacksrichtungKatForm(forms.ModelForm):

    #beschreibung = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = GeschmacksrichtungKategorie

class Wein(BaseProduct):
	listed = models.BooleanField(verbose_name='Im Shop gelistet', default=True)
	img = models.ImageField(verbose_name='Produkt Bild',upload_to='produktbilder')
	lage =  models.CharField(max_length=2, choices=LAGEN_AUSWAHL,blank=True, null=True, default=0)
	jahrgang = models.CharField(verbose_name='Jahrgang', max_length=4)
	apnr = models.CharField(max_length=255,verbose_name='A.P.Nr',blank=True, null=True)
	sauere = models.FloatField(verbose_name='Gesamtsäure')
	suesse = models.FloatField(verbose_name='Restsüße')
	sulfite = models.BooleanField(verbose_name='enthält Sulfite', default=True)
	geschmack = models.ForeignKey('GeschmacksrichtungKategorie',blank=True, null=True)
	#geschmack = models.CharField(max_length=2000,verbose_name='Geschmack',blank=True, null=True)
	alk = models.FloatField(verbose_name='Alkoholgehalt')
	vol = models.FloatField(verbose_name='Nennvolumen')
	bouquet = models.CharField(max_length=2000,verbose_name='Bouquet',blank=True, null=True)
	auszeichnung= models.ManyToManyField('auszeichnungen.Auszeichnung',blank=True, null=True)
	kat = models.ForeignKey('LageKategorie',blank=True, null=True)
	art = models.ForeignKey('ArtKategorie',blank=True, null=True)

	

	# TODO
	# Im Backend Bild anzeigen
	# Lagen abfragen für die Lagen Auswahl
	# Kategorien und Art in Weinshop integrieren
	# Kategorie mit Info text
	

	class Meta: 
		ordering = ['slug']
		verbose_name_plural = "Weine"
class WeinForm(forms.ModelForm):
	
	bouquet = forms.CharField( widget=forms.Textarea,required=False )
	class Meta:
		model = Wein
		#fields = ['name','slug','active','unit_price','listed','img', 'lage','jahrgang', 'sauere','suesse', 'alk', 'vol','auszeichnung']

class myOrder(BaseOrder):
	emailForConfirm = models.CharField(max_length=255,verbose_name='Kontaktemailadresse')

	shipPrename = models.CharField(max_length=255,verbose_name='Vorname')
	shipSurname = models.CharField(max_length=255,verbose_name='Nachname')
	shipStreet = models.CharField(max_length=255)
	shipNr = models.CharField(max_length=255)
	shipZipCode = models.CharField(max_length=255)
	shipTown = models.CharField(max_length=255)
	shipLand = models.CharField(max_length=255)
	shipTel = models.CharField(max_length=255)
	shipFax = models.CharField(max_length=255)

	billPrename = models.CharField(max_length=255)
	billSurname = models.CharField(max_length=255)
	billStreet = models.CharField(max_length=255)
	billNr = models.CharField(max_length=255)
	billZipCode = models.CharField(max_length=255)
	billTown = models.CharField(max_length=255)
	billLand = models.CharField(max_length=255)
	billTel = models.CharField(max_length=255)
	billFax = models.CharField(max_length=255)


	objects = OrderManager()

	class Meta:
		verbose_name_plural = 'Bestellungen'
		verbose_name = 'Bestellung'
   