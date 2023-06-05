from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class MapaView(TemplateView):
    template_name = 'mapa.html'