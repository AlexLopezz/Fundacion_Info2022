from django.shortcuts import render
from django.views.generic import ListView
from .models import Evento
# Create your views here.
class ListaEventos(ListView):
    model = Evento
    template_name = 'eventos/seccion_eventos.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(estado=True)
        return queryset
