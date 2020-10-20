"""Streamfields for flex page and all other pages."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your title' ) #required é come null e blanket mixati insieme
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"
    
class RichtextBlock(blocks.RichTextBlock):
     
     class Meta: #noqa
         template = "streams/richtext_block.html"
         icon = "edit"
         label = "Full RichText"

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text='Add your title' )

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=False, max_length=200)),
                ("text", blocks.TextBlock(required=False, max_length=300)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first")),

            ]
        )
    )
    
    class Meta: #noqa
         template = "streams/card_block.html"
         icon = "edit"
         label = "Cards"