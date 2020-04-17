"""flexible page.""" 

from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks

class FlexPage(Page):
    
    template = "flex/flex_page.html"

    
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichtextBlock()),
            ("cards", blocks.CardBlock()),
    ], 
    
    null=True,
    blank=True
    
    )

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null= True,  
        blank= False, 
        on_delete= models.SET_NULL,
        related_name="+",
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),    
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("content"),
    ]
    
    class Meta: #noqa
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"


