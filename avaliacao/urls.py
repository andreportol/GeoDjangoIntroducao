from django.urls import path

from .views import AvaliacaoImobGeoJson

app_name = 'avaliacao'

urlpatterns = [
    path('',AvaliacaoImobGeoJson.as_view(), name='avaliacao_geojson' )
]
