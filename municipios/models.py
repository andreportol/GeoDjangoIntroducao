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

    @property
    def popup_content(self):
        popup =  f'<div><u><b>Município:</b></u> {self.nm_mun} </div>'
        popup += f'<div><u><b>Sigla:</b></u> {self.sigla_uf} </div>'
        popup += f'<div><u><b>Área:</b></u> {self.area_km2} </div>'
        return popup