# -*- coding: utf-8 -*-
import inspect
from django.db import models
from cms.models.fields import PlaceholderField
from cms.plugin_rendering import render_placeholder
from zinnia.models_bases.entry import AbstractEntry

class EntryExtrafields(AbstractEntry):
	content_placeholder = PlaceholderField('content')
	source = models.CharField(max_length=255, verbose_name="Quelle", blank=True,help_text="Dieses Feld bitte nur für Presseartikel ausfüllen.")
	author = models.CharField(max_length=255, verbose_name="Autor", blank=True,help_text="Dieses Feld bitte nur für Presseartikel ausfüllen.")
	month = models.CharField(max_length=255, verbose_name="Monat des Erscheinens",blank=True, help_text="Dieses Feld bitte nur für Presseartikel ausfüllen.")

	def acquire_context(self):
		frame = None
		try:
			for f in inspect.stack()[1:]:
				frame = f[0]
				args, varargs, keywords, alocals = inspect.getargvalues(frame)
				if 'context' in args:
					return alocals['context']
		finally:
			del frame
	@property
	def html_content(self):
		context = self.acquire_context()
		return render_placeholder(self.content_placeholder, context)

	def __unicode__(self):
		return u'Blogeintrag %s' % self.title

	class Meta(AbstractEntry.Meta):
		abstract = True
