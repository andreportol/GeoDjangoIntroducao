from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import Municipios_MS


class Municipios_MSGeoJson(GeoJSONLayerView):
    model = Municipios_MS
    properties = ['popup_content',]

class Municipios_Cadastro(TemplateView):
    template_name = 'formulario_cadastro.html'