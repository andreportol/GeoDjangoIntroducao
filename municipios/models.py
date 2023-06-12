# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Municipios_MS(models.Model):
    cd_mun = models.CharField(max_length=7)
    nm_mun = models.CharField(max_length=50)
    sigla_uf = models.CharField(max_length=2)
    area_km2 = models.FloatField()
    geom = models.MultiPolygonField(srid=4674)

    def __str__(self):
        return self.nm_mun
