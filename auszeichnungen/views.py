from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from auszeichnungen.models import Auszeichnung

class IndexView(generic.ListView):
	template_name = 'auszeichnungen/index.html'
	context_object_name = 'alle_auszeichnungen'

	def get_queryset(self):
		return Auszeichnung.objects.all()