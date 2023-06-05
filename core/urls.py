from django.urls import path

from .views import IndexView, MapaView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('mapa/', MapaView.as_view(), name='mapa')
]
