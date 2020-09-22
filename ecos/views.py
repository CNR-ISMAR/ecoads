from django.shortcuts import render
from django.core.serializers import serialize
import json

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import DataSource, Parameter, EcosSite

class EcosSiteList(ListView):
    
    model = EcosSite
    template_name = 'ecossite_list.html'


class EcosSiteDetailView(DetailView):

    model = EcosSite
    template_name = 'ecos/ecossite_detail.html'
    slug_field = 'suffix'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singlesite'] = [self.object.location.y, self.object.location.x]
        context['denomination'] = self.object.denomination
        if self.object.domain_area is not None:
            context['polygon'] = json.loads(serialize('geojson', [self.object],
                geometry_field='domain_area',
                fields=('denomination',)))
        return context
