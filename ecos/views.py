from django.shortcuts import render
from django.core.serializers import serialize
import json

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from .models import Parameter, EcosSite, InfoResource
from measurements.models import Station, Location

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
    
    model = Location
    template_name = 'ecos/fix_point_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fix_point'] = [(s.label, s.geo.centroid.y, s.geo.centroid.x, s.id, s.image) for s in Location.objects.all()]
        context['fix_label'] = Location.label
        if Station.image is not None:
            context['fix_img'] = Location.image
        # fix = []
        # for s in Station.objects.all() if s.location is not None:
        #     fix.append(s.fix)
        return context

class InfoResourceList(ListView):
    
    model = InfoResource
    template_name = 'ecos/info_resource_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] =  [(s.title ) for s in InfoResource.objects.all()]
        return context

class InfoResourceDetailView(DetailView):

    model = InfoResource
    template_name = 'ecos/info_resource_detail.html'
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context

class EcosSiteDetailView(DetailView):

    model = EcosSite
    template_name = 'ecos/ecossite_detail.html'
    slug_field = 'suffix'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['singlesite'] = [self.object.location.y, self.object.location.x]
        context['denomination'] = self.object.denomination
        context['n2k']= self.object.is_n2k
        if self.object.domain_area is not None:
            context['polygon'] = json.loads(serialize('geojson', [self.object],
                geometry_field='domain_area',
                fields=('denomination',)))
        return context


class FixPointView(DetailView):

    model = Location
    template_name = 'ecos/fix_point.html'
    slug_field = 'id' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = self.object.label
        context['fixsinglesite'] = [self.object.geo.centroid.y, self.object.geo.centroid.x]
        context['prova'] = Location.objects.get(pk=self.object.id).station_set.all()
        stationlabel = []
        for l in Location.objects.get(pk=self.object.id).station_set.all():
            context['stationlabel'] = l.label
        
        context['sito'] = Location.objects.get(pk=self.object.id).ecossite_set.all()
        sitolocation = []
        for l in Location.objects.get(pk=self.object.id).ecossite_set.all():
            context['sitolocation'] = l.suffix
        
        return context


class FixDataView(DetailView):

    model = Station
    template_name = 'ecos/fix_point_data.html'
    slug_field = 'id' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['label'] = self.object.label
        context['fixsinglesite'] = [self.object.location.geo.centroid.y, self.object.location.geo.centroid.x]
        
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

class EcosSiteToolsContributionView(DetailView):

    model = EcosSite
    template_name = 'ecos/ecossite_tools_contribution.html'
    slug_field = 'suffix'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EcosSiteToolsConservationView(DetailView):

    model = EcosSite
    template_name = 'ecos/ecossite_tools_conservation.html'
    slug_field = 'suffix'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context