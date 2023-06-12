from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Municipios_MS


@admin.register(Municipios_MS)
class MunicipiosAdmin(LeafletGeoAdmin):
    list_display= [
            'cd_mun', 'nm_mun','area_km2'
    ]
