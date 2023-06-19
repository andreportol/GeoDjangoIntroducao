from django.urls import path

from .views import AreasPublicasCreateView

app_name = 'areas_publicas'

urlpatterns = [
    path('inserir_area/', AreasPublicasCreateView.as_view(),name='areas_CreateView'),
]
