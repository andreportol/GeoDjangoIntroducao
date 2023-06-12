from djgeojson.views import GeoJSONLayerView

from .models import AvaliacaoImob


class AvaliacaoImobGeoJson(GeoJSONLayerView):
    model = AvaliacaoImob