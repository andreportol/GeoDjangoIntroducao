from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import AvaliacaoImob


@admin.register(AvaliacaoImob)
class AvaliacaoImobAdmin(LeafletGeoAdmin):
    list_display= [
            'informante', 'data', 'parcelamen', 'testada', 'areaterren', 'preco', 'quadra'
        ]
