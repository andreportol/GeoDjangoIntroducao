import os

from django.contrib.gis.utils import LayerMapping

from .models import AvaliacaoImob

# Auto-generated `LayerMapping` dictionary for AvaliacaoImob model
avaliacaoimob_mapping = {
    'objectid': 'objectid',
    'informante': 'informante',
    'data': 'data',
    'parcelamen': 'parcelamen',
    'testada': 'testada',
    'areaterren': 'areaterren',
    'preco': 'preco',
    'quadra': 'quadra',
    'lote': 'lote',
    'endereco': 'endereco',
    'inscant': 'inscant',
    'bairro': 'bairro',
    'regiao': 'regiao',
    'observacao': 'observacao',
    'pavimentac': 'pavimentac',
    'n_testadas': 'n_testadas',
    'preco_un': 'preco_un',
    'contato_in': 'contato_in',
    'formatoter': 'formatoter',
    'topografia': 'topografia',
    'fat_fonte': 'fat_fonte',
    'indice': 'indice',
    'created_us': 'created_us',
    'created_da': 'created_da',
    'last_edite': 'last_edite',
    'last_edi_1': 'last_edi_1',
    'geom': 'POINT',
}

shp = os.path.abspath(os.path.join('dados', 'avaliacao.shp'))


def run_avaliacaoImob(verbose=True):
    lm = LayerMapping(AvaliacaoImob, shp, avaliacaoimob_mapping)
    lm.save(strict=True, verbose=True)