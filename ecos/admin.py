from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from wagtail.admin.edit_handlers import FieldPanel
from wagtailleafletwidget.edit_handlers import GeoPanel
from .models import DataSource, Parameter, EcosSite, EcosSitesDataSources, ParametersDataSources


class DataSourceAdmin(ModelAdmin):
    """DataSource admin."""

    model = DataSource
    menu_label = "Data Source"
    menu_icon = "folder"
    menu_order = 500
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("name", "observation_model", "update_frequency", "sampling_frequency", "temporal_resolution", "temporal_coverage",)
    search_field = ("name", "observation_model", "update_frequency", "sampling_frequency", "temporal_resolution", "temporal_coverage",)
      
    panels =[
         FieldPanel("name"),
         FieldPanel("observation_model"),
         GeoPanel("location"),
         #GeoPanel("domain_area"), #tofix 
         FieldPanel("update_frequency"),
         FieldPanel("sampling_frequency"),
         FieldPanel("temporal_resolution"),
         FieldPanel("temporal_coverage"),
    ] 

modeladmin_register(DataSourceAdmin)

class ParameterAdmin(ModelAdmin):
    """Parameter admin."""

    model = Parameter
    menu_label = "Parameter"
    menu_icon = "edit"
    menu_order = 600
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("uri", "preferred_label_en", "definition_en",)
    search_field = ("uri", "preferred_label_en", "definition_en",)

modeladmin_register(ParameterAdmin)

class EcosSiteAdmin(ModelAdmin):
    """EcosSite admin."""

    model = EcosSite
    menu_label = "EcosSite"
    menu_icon = "tick"
    menu_order = 700
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("denomination", "description", "website")
    search_field = ("denomination", "description", "website")

    panels =[
    FieldPanel("denomination"),
    FieldPanel("description"),
    #GeoPanel("domain_area"), #tofix poligono e non location!
    GeoPanel("location"),
    FieldPanel("website"),
    FieldPanel("is_ecoss"),
    ] 

modeladmin_register(EcosSiteAdmin)

class EcosSitesDataSourcesAdmin(ModelAdmin):
    """EcosSitesDataSources admin."""

    model = EcosSitesDataSources
    menu_label = "M2M EcosSites/DataSources"
    menu_icon = "success"
    menu_order = 800
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("ecos_site", "data_source",)
    search_field = ("ecos_site", "data_source",)

modeladmin_register(EcosSitesDataSourcesAdmin)

class ParametersDataSourcesAdmin(ModelAdmin):
    """ParametersDataSources admin."""

    model = ParametersDataSources
    menu_label = "M2M Parameters/DataSources"
    menu_icon = "pick"
    menu_order = 900
    add_to_settings_menu = False 
    exclude_from_explorer = False
    list_display = ("parameter", "data_source",)
    search_field = ("parameter", "data_source",)

modeladmin_register(ParametersDataSourcesAdmin)

