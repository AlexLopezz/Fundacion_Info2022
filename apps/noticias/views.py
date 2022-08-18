from django.shortcuts import render
from apps.noticias.models import Noticia 
from django.views.generic import ListView, DetailView
# Create your views here.

class noticias(ListView):
    model = Noticia
    template_name = 'noticias/seccion_noticias.html'

class articulo(DetailView):
    model = Noticia
    template_name = 'noticias/articulo.html'