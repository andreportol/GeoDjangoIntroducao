from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('municipios/', include('municipios.urls')),
    path('areaspublicas/', include('areas_publicas.urls'))
]
