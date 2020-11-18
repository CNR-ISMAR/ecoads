"""Conceptual model page."""

from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class CMPage(Page):

    template = "ecos_cm/cm_page.html"


    ECOLOGICAL_PROCESSES = "ecological processes"
    TARGET_SPECIES = "target species"
    
    CONCELTUAL_MODEL_TYPE_CHOICES = [
        (ECOLOGICAL_PROCESSES,'ecological processes'),
        (TARGET_SPECIES, 'target species'),
    ]
    conceptual_model_type = models.CharField(
      choices=CONCELTUAL_MODEL_TYPE_CHOICES,
      max_length=100,
      default=ECOLOGICAL_PROCESSES,
    )

    

    cm_title = models.CharField(max_length=300, null=True, blank=True)
    cm_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    cm_human_interactions = RichTextField( null=True, blank=True)
    cm_ecolagical_processes = RichTextField( null=True, blank=True)
    cm_oceanographic_variables = RichTextField( null=True, blank=True)
    cm_performance_indicators = RichTextField( null=True, blank=True)



    content_panels = Page.content_panels + [
        FieldPanel("conceptual_model_type"),
        FieldPanel("cm_title"),
        ImageChooserPanel("cm_image"),
        FieldPanel("cm_human_interactions"),
        FieldPanel("cm_ecolagical_processes"),
        FieldPanel("cm_oceanographic_variables"),
        FieldPanel("cm_performance_indicators"),
    ]

    


