from django.shortcuts import render
from django.core.serializers import serialize
import json

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import DataSource, Parameter, EcosSite

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
        elif sitetype == 'fixoss':
            return EcosSite.objects.filter(is_fixoss = True )
        elif sitetype == 'ecoss':
            return EcosSite.objects.filter(is_ecoss = True )
        else:
            return EcosSite.objects.all()



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


class EcosSiteDashboard(ListView):

    model = EcosSite
    template_name = 'ecos/ecossite_dashboard.html'
    #slug_field = 'suffix'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['singlesite'] = [self.object.location.y, self.object.location.x]
    #     context['denomination'] = self.object.denomination
    #     if self.object.domain_area is not None:
    #         context['polygon'] = json.loads(serialize('geojson', [self.object],
    #             geometry_field='domain_area',
    #             fields=('denomination',)))
    #     return context
