"""Ecological observatory system models."""

from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from wagtail.admin.edit_handlers import FieldPanel
from ecos_cm.models import CMPage
from measurements.models import Location
from measurements.models import Station


# class DataSource(models.Model):
#     name = models.CharField(max_length=200, blank=True, null=False)
#     observation_model = models.CharField(max_length=200, blank=True, null=False)
#     location = models.PointField(blank=False, null=True )
#     domain_area =data_source = models.ManyToManyField(DataSource, through='EcosSitesDataSources') 
#     parameters = models.ManyToManyField(Parameter, throug models.MultiPolygonField(blank=False, null=True )
#     update_frequency = models.CharField(max_length=200, blank=True, null=False)
#     sampling_frequency = models.CharField(max_length=200, blank=True, null=False)
#     temporal_resolution = models.CharField(max_length=200, blank=True, null=False)
#     temporal_coverage = models.CharField(max_length=200, blank=True, null=False)
#     parameters = models.ManyToManyField("Parameter", through='DataSourcesParameters')
#     #measurement_id = models.IntegerField(blank=True, null=True)

#     def __str__(self): 
#         return self.name


class Parameter(models.Model):
    uri = models.URLField(max_length=600,blank=False, null=True )  
    preferred_label_en = models.CharField(max_length=500, blank=False, null=True)
    definition_en = models.TextField(blank=False, null=True)
    
    def __str__(self): 
        return self.preferred_label_en


class EcosSite(models.Model):
    data = JSONField(blank=True, null=True)
    suffix = models.CharField(max_length=200, blank=False, null=True)
    denomination = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    domain_area = models.MultiPolygonField(blank=True, null=True)  #polygon
    location = models.PointField() # marker point 
    website = models.URLField(max_length=600,blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    is_ecoss = models.BooleanField(default=False)
    is_n2k = models.BooleanField(default=False)
    is_lter = models.BooleanField(default=False)
    is_fixoss = models.BooleanField(default=False)
    is_onmap = models.BooleanField(default=False)
    img = models.URLField(max_length=600,blank=True, null=True)
    #measurement_id = models.IntegerField(blank=True, null=True)
    #tutte le location che cadono in quest'area - script @todo
    measurement_location_id = models.ManyToManyField(Location, through='EcosSitesLocationDjangoMeasurements', blank=True)
    #data_source = models.ManyToManyField(DataSource, through='EcosSitesDataSources') 
    parameters = models.ManyToManyField(Parameter, through='EcosSitesParameters', blank=True)
    conceptualmodels = models.ManyToManyField(CMPage, through='EcosSitesCMPages', blank=True )
   
    def __str__(self):
        return self.denomination


class EcosSitesParameters(models.Model): 
    ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE) 


class EcosSitesLocationDjangoMeasurements(models.Model): 
    ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE) 
    measurement_locationid = models.ForeignKey(Location, on_delete=models.CASCADE)


class EcosSitesCMPages(models.Model): 
    ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE) 
    conceptualmodels = models.ForeignKey(CMPage, on_delete=models.CASCADE)



# class EcosSitesDataSources(models.Model): 
#     ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE)
#     data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)


# class DataSourcesParameters(models.Model): 
#     parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE) 
#     data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)