from django.db import models
from django.utils.functional import cached_property
from django.core.serializers import serialize
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from ecos.models import EcosSite
from measurements.models import Station, Location
import json

class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"  
    max_count = 1 #only 1 homepage in the site

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = models.CharField(max_length=100, blank=False, null=True) 

    banner_cta = models.ForeignKey( 
        "wagtailcore.Page",
        null= True,  
        blank= True, 
        on_delete= models.SET_NULL,
        related_name="+",
    )  

    content_panels = Page.content_panels + [
         FieldPanel("banner_title"),    
         FieldPanel("banner_subtitle"),
         #FieldPanel("body"),
         PageChooserPanel("banner_cta"),
    ]

    def get_context(self, request):
      context = super(HomePage, self).get_context(request)
      context['ecossites'] = [(s.denomination, s.location.y, s.location.x, s.suffix) for s in EcosSite.objects.filter(is_ecoss=True)]
      context['ltersites'] = [(s.denomination, s.location.y, s.location.x, s.suffix) for s in EcosSite.objects.filter(is_lter=True)]
      context['n2ksites'] = [(s.denomination, s.location.y, s.location.x, s.suffix) for s in EcosSite.objects.filter(is_n2k=True)]
      context['other_ecossites'] = [(s.denomination, s.location.y, s.location.x, s.suffix) for s in EcosSite.objects.filter(is_onmap=True)]
      context['polygons'] = json.loads(serialize('geojson', EcosSite.objects.filter(is_ecoss=True),
        geometry_field='domain_area',
        fields=('denomination',))),
      context['polygons_n2k'] = json.loads(serialize('geojson', EcosSite.objects.filter(is_n2k=True),
        geometry_field='domain_area',
        fields=('denomination',))),
      context['polygons_lter'] = json.loads(serialize('geojson', EcosSite.objects.filter(is_lter=True),
        geometry_field='domain_area',
        fields=('denomination',))),
      context['fix_point'] = [(s.location.label, s.location.geo.centroid.y, s.location.geo.centroid.x, s.id) for s in Station.objects.all() if s.location is not None]
      return context 
