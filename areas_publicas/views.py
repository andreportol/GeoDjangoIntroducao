from django.views.generic import CreateView

#from .forms import InsereAreaPublicaForm
from .models import InserirAreaPublica


class AreasPublicasCreateView(CreateView):
    template_name = 'formulario_cadastro.html'
    model = InserirAreaPublica
    fields = '__all__'
 #   form_class = InsereAreaPublicaForm


