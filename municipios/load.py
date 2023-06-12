import os

from django.contrib.gis.utils import LayerMapping

from municipios.models import Municipios_MS

shp = os.path.abspath(os.path.join('dados', 'MS_Municipios_2022.shp'))


# Auto-generated `LayerMapping` dictionary for Municipios_MS model
municipios_ms_mapping = {
    'cd_mun': 'CD_MUN',
    'nm_mun': 'NM_MUN',
    'sigla_uf': 'SIGLA_UF',
    'area_km2': 'AREA_KM2',
    'geom': 'MULTIPOLYGON',
}

def run_MS_Municipios(verbose=True):
    lm = LayerMapping(Municipios_MS, shp, municipios_ms_mapping)
    lm.save(strict=True, verbose=True)