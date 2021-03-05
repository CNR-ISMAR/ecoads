"""Ecological observatory system models."""

from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from wagtail.admin.edit_handlers import FieldPanel
from ecos_cm.models import CMPage


class DataSource(models.Model):
    name = models.CharField(max_length=200, blank=True, null=False)
    observation_model = models.CharField(max_length=200, blank=True, null=False)
    location = models.PointField(blank=False, null=True )
    domain_area = models.MultiPolygonField(blank=False, null=True )
    update_frequency = models.CharField(max_length=200, blank=True, null=False)
    sampling_frequency = models.CharField(max_length=200, blank=True, null=False)
    temporal_resolution = models.CharField(max_length=200, blank=True, null=False)
    temporal_coverage = models.CharField(max_length=200, blank=True, null=False)
    parameters = models.ManyToManyField("Parameter", through='DataSourcesParameters')

    def __str__(self): 
        return self.name


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
    description = models.TextField(blank=False, null=True)
    domain_area = models.MultiPolygonField(blank=False, null=True)  #polygon
    location = models.PointField() # marker point 
    website = models.URLField(max_length=600,blank=False, null=True)
    last_update = models.DateTimeField(blank=False, null=True)
    is_ecoss = models.BooleanField(default=False)
    is_n2k = models.BooleanField(default=False)
    is_lter = models.BooleanField(default=False)
    is_fixoss = models.BooleanField(default=False)
    img = models.URLField(max_length=600,blank=False, null=True)
    data_source = models.ManyToManyField(DataSource, through='EcosSitesDataSources') 
    parameters = models.ManyToManyField(Parameter, through='EcosSitesParameters')
    conceptualmodels = models.ManyToManyField(CMPage, through='EcosSitesCMPages')
   
    def __str__(self):
        return self.denomination


class EcosSitesParameters(models.Model): 
    ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE) 


class EcosSitesDataSources(models.Model): 
    ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)


class DataSourcesParameters(models.Model): 
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE) 
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)

class EcosSitesCMPages(models.Model): 
    ecos_site = models.ForeignKey(EcosSite, on_delete=models.CASCADE) 
    conceptualmodels = models.ForeignKey(CMPage, on_delete=models.CASCADE)


class Serie(models.Model):
    site_data_source = models.ForeignKey(EcosSitesDataSources, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    height = models.FloatField(blank=True, null=True)

    def __str__(self):
        return u'{} - {}'.format(self.site_data_source, self.parameter)


class Measure(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(db_index=True)
    value = models.FloatField()

    class Meta:
        unique_together = ('serie', 'timestamp', 'value')
