from unicodedata import category
from django.shortcuts import render
from apps.noticias.models import Categoria, Noticia 
from django.views.generic import ListView, DetailView
# Create your views here.

class noticias(ListView):
    model = Noticia
    template_name = 'noticias/seccion_noticias.html'
    
    def get_context_data(self, *args, **kwargs):
        categoria_menu = Categoria.objects.all()
        ctx = super(noticias, self).get_context_data(*args, **kwargs)

        ctx['categoria'] = categoria_menu
        return ctx

class articulo(DetailView):
    model = Noticia
    template_name = 'noticias/articulo.html'

def categoria(request, cat):
    cat_object = Categoria.objects.get(pk=cat)
    noticias_categoria = Noticia.objects.filter(categoria= cat)
    return render(request, 'noticias/categoria.html',{'nombre': cat_object.nombre,'noticias_cat': noticias_categoria})

def mision(request):
    return render(request, 'noticias/mision.html')

def somos(request):
    return render(request, 'noticias/somos.html')   
    