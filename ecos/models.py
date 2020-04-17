"""Ecological observatory system models."""

from django.db import models
from django.contrib.gis.db import models

class Directive(models.Model):
    directive_name = models.CharField(max_length=200)

    def _str_(self): 
        return self.directive_name

class Parameter(models.Model):
    parameter_name = models.CharField(max_length=200)
    #choices  array 
    #@todo lista in attesa del confronto con gli altri 

    def _str_(self): 
        return self.parameter_name

class DataSource(models.Model):
    datasource_name= models.CharField(max_length=200, blank=True, null=False)

    def _str_(self): 
        return self.datasource_name

class EcoadsSite(models.Model):
    denomination = models.CharField(max_length=200)
    description = models.TextField()
    domain_area = models.MultiPolygonField()  #il poligono
    location = models.GeometryField() #il punto che lo identifica
    website = models.CharField(max_length=600) #link
    parameters = models.ManyToManyField(Parameter, through='EcoadsSitesParameters')  
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)


    def _str_(self):
        return self.denomination


class EcoadsSitesParameters(models.Model): 
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    ecoadsSite = models.ForeignKey(EcoadsSite, on_delete=models.CASCADE)
    #qui aggiungo le colonne che voglio in più
    