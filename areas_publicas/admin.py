from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import InserirAreaPublica


@admin.register(InserirAreaPublica)
class InserirAreaPublicaAdmin(LeafletGeoAdmin):
    list_display= [
            'inscant', 'nome_invasor', 'rua', 'numero', 'bairro', 'nome_auditor', 'data', 'geom'
    ]



