from django.shortcuts import render
from django.core.serializers import serialize
import json

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Parameter, EcosSite
from measurements.models import Station
#from .models import DataSource

from django.http import JsonResponse

def sitesjson(request):
    data = []
    for s in EcosSite.objects.filter(is_ecoss = True ):
        data.append(s.data)
    return JsonResponse(data, safe=False)
    
class EcosSiteList(ListView):
    
    model = EcosSite
    template_name = 'ecossite_list.html'
    def get_queryset(self): 
        sitetype = self.kwargs.get('sitetype')
        if sitetype == 'natura2000':
            return EcosSite.objects.filter(is_n2k = True )
        elif sitetype == 'lter':
            return EcosSite.objects.filter(is_lter = True )
        # elif sitetype == 'fixoss':
        #    return EcosSite.objects.filter(is_fixoss = True )
        elif sitetype == 'ecoss':
            return EcosSite.objects.filter(is_ecoss = True )
        else:
            return EcosSite.objects.all()


class FixPointList(ListView):
    
    model = Station
    template_name = 'ecos/fix_point_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fix_point'] = [(s.location.label, s.location.geo.centroid.y, s.location.geo.centroid.x, s.id) for s in Station.objects.all() if s.location is not None]
        context['fix_label'] = Station.label
        # fix = []
        # for s in Station.objects.all() if s.location is not None:
        #     fix.append(s.fix)
        return context


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


class FixPointView(DetailView):

    model = Station
    template_name = 'ecos/fix_point.html'
    slug_field = 'id' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = self.object.label
        return context


class EcosSiteDashboardView(DetailView):

    model = EcosSite
    template_name = 'ecos/ecossite_dashboard.html'
    slug_field = 'suffix'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = "https://ecoads.eu/measurements/d/hvh9-qyGk/test?orgId=1"
       
        var = []
        for location in self.object.measurement_location_id.all():   
            var.append('&var-location=' + str(location.id))
            context['var'] ="".join(var)
            context['theme'] = '&theme=light&kiosk=tv'
        return context
