from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Solicitud
from .forms import SolicitudForm 
from django.shortcuts import render

# Create your views here.
class CrearSoicitudView(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    success_url = reverse_lazy('inicio')

    """ def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form) """