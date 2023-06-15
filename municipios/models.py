# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Municipios_MS(models.Model):
    cd_mun = models.CharField(max_length=7, verbose_name='Código Município')
    nm_mun = models.CharField(max_length=50, verbose_name='Nome Município')
    sigla_uf = models.CharField(max_length=2, verbose_name='Sigla')
    area_km2 = models.FloatField(verbose_name='Área_km2')
    geom = models.MultiPolygonField(srid=4674)

    def __str__(self):
        return self.nm_mun

    @property
    def popup_content(self):
        popup =  f'<div><u><b>Município:</b></u> {self.nm_mun} </div>'
        popup += f'<div><u><b>Sigla:</b></u> {self.sigla_uf} </div>'
        popup += f'<div><u><b>Área:</b></u> {self.area_km2} </div>'
        return popup
    
    class Meta:
        verbose_name = "Município"
        verbose_name_plural = "Municípios"