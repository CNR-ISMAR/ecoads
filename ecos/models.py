"""Ecological observatory system models."""

from django.db import models
from django.contrib.gis.db import models
from wagtail.admin.edit_handlers import FieldPanel

class DataSource(models.Model):
    name = models.CharField(max_length=200, blank=True, null=False)
    observation_model = models.CharField(max_length=200, blank=True, null=False)
    location = models.PointField(blank=False, null=True )
    #variables = models.TextField(blank=False, null=True )
    domain_area = models.MultiPolygonField(blank=False, null=True )
    update_frequency = models.CharField(max_length=200, blank=True, null=False)
    sampling_frequency = models.CharField(max_length=200, blank=True, null=False)
    temporal_resolution = models.CharField(max_length=200, blank=True, null=False)
    temporal_coverage = models.CharField(max_length=200, blank=True, null=False)

    def _str_(self): 
        return self.name



class Parameter(models.Model):
    uri = models.URLField(max_length=600,blank=False, null=True )  
    preferred_label_en = models.CharField(max_length=500, blank=False, null=True)
    definition_en = models.TextField(blank=False, null=True)
    data_source = models.ManyToManyField(DataSource, through='ParametersDataSources')

    def _str_(self): 
        return self.preferred_label_en

class EcosSite(models.Model):
    suffix = models.CharField(max_length=200, blank=False, null=True)
    denomination = models.CharField(max_length=200)
    description = models.TextField(blank=False, null=True)
    domain_area = models.MultiPolygonField(blank=False, null=True)  #il poligono
    location = models.PointField() #il punto che lo identifica
    website = models.URLField(max_length=600,blank=False, null=True)
    last_update = models.DateTimeField(blank=False, null=True)
    is_ecoss = models.BooleanField(default=False)
    data_source = models.ManyToManyField(DataSource, through='EcosSitesDataSources') 


    def _str_(self):
        return self.denomination

class EcosSitesDataSources(models.Model): 
    ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    
class ParametersDataSources(models.Model): 
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE) 
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
