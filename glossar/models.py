from django.db import models
from django.forms import ModelForm

class Term(models.Model):
	title = models.CharField(max_length=255, verbose_name='Titel')
	description = models.TextField(max_length=1000, verbose_name='Beschreibung')
	def __unicode__(self):
		return u'Begriff %s' % self.title
	class Meta: 
		verbose_name = 'Begriff'
		verbose_name_plural = 'Begriffe'

class TermForm(ModelForm):

    class Meta:
        model = Term
        fields = ['title', 'description']



