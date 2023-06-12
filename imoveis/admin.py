from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Imoveis


@admin.register(Imoveis)
class ImoveisAdmin(LeafletGeoAdmin):
    list_display= ['codlote', 'usoimovel', 'inscant', 'ruaimo', 'nrporta']
 