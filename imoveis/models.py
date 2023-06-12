# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Imoveis(models.Model):
    codlote = models.CharField(max_length=11, blank=True, null=True)
    codelote = models.CharField(max_length=11, blank=True, null=True)
    inscant = models.CharField(max_length=11, blank=True, null=True)
    tipoloc = models.CharField(max_length=10, blank=True, null=True)
    ruaimo = models.CharField(max_length=50, blank=True, null=True)
    nrporta = models.BigIntegerField(blank=True, null=True)
    complement = models.CharField(max_length=16, blank=True, null=True)
    parcelamen = models.CharField(max_length=50, blank=True, null=True)
    patrimonio = models.CharField(max_length=36, blank=True, null=True)
    usoimovel = models.CharField(max_length=36, blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    shape_len = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=31981, blank=True, null=True)

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
    
    def __str__(self):
        return self.inscant
