"""ecos features page."""

from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class Features(Page):

    template = "ecos_features/features.html"
    

    features_title = models.CharField(max_length=300, null=True, blank=True)
   

    content_panels = Page.content_panels + [
        FieldPanel("features_title"),
    ]

    


