from django.urls import path

from .views import Municipios_MSGeoJson

app_name = 'municipios'

urlpatterns = [
    path('',Municipios_MSGeoJson.as_view(), name='municipios_geojson' ),
]