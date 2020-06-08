from django.db import models
from django.utils.functional import cached_property
from django.core.serializers import serialize
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from ecos.models import EcosSite
import json

class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"  
    max_count = 1 #only 1 homepage in the site

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = models.CharField(max_length=100, blank=False, null=True) 
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null= True,  
        blank= False, 
        on_delete= models.SET_NULL,
        related_name="+",
    )
    body = RichTextField(null=True)

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
         FieldPanel("body"),
         ImageChooserPanel("banner_image"),
         PageChooserPanel("banner_cta"),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        #context['ecossites'] = EcosSite.objects.all()
        context['ecossites'] = [(s.denomination, s.location.y, s.location.x) for s in EcosSite.objects.filter(is_ecoss=True)]
        #context['polygons'] = [s.domain_area for s in EcosSite.objects.all()]
        context['other_ecossites'] = [(s.denomination, s.location.y, s.location.x) for s in EcosSite.objects.filter(is_ecoss=False)]
        context['polygons'] = json.loads(serialize('geojson', EcosSite.objects.filter(is_ecoss=True),
          geometry_field='domain_area',
          fields=('denomination',)))
        return context