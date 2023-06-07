import os

from django.contrib.gis.utils import LayerMapping

from .models import Imoveis

# Auto-generated `LayerMapping` dictionary for Imoveis model
imoveis_mapping = {
    'codlote': 'CODLOTE',
    'codelote': 'CODELOTE',
    'inscant': 'INSCANT',
    'tipoloc': 'TIPOLOC',
    'ruaimo': 'RUAIMO',
    'nrporta': 'NRPORTA',
    'complement': 'COMPLEMENT',
    'parcelamen': 'PARCELAMEN',
    'patrimonio': 'PATRIMONIO',
    'usoimovel': 'USOIMOVEL',
    'shape_area': 'SHAPE_AREA',
    'shape_len': 'SHAPE_LEN',
    'geom': 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join('dados', 'imoveis.shp'))

def run_imoveis(verbose=True):
    lm = LayerMapping(Imoveis, shp, imoveis_mapping)
    lm.save(strict=True, verbose=True)