from unicodedata import category
from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
from apps.noticias.models import Noticia 
=======
from apps.noticias.models import Categoria, Noticia 
>>>>>>> Jorge
=======
from apps.noticias.models import Categoria, Noticia 
>>>>>>> 70dda3e4ca0ff21c9524a9a5e8993a7a407678a4
from django.views.generic import ListView, DetailView
# Create your views here.

class noticias(ListView):
    model = Noticia
    template_name = 'noticias/seccion_noticias.html'
<<<<<<< HEAD
<<<<<<< HEAD
=======
    
    def get_context_data(self, *args, **kwargs):
        categoria_menu = Categoria.objects.all()
        ctx = super(noticias, self).get_context_data(*args, **kwargs)

        ctx['categoria'] = categoria_menu
        return ctx
>>>>>>> 70dda3e4ca0ff21c9524a9a5e8993a7a407678a4

class articulo(DetailView):
    model = Noticia
    template_name = 'noticias/articulo.html'
<<<<<<< HEAD
=======
    
    def get_context_data(self, *args, **kwargs):
        categoria_menu = Categoria.objects.all()
        ctx = super(noticias, self).get_context_data(*args, **kwargs)

        ctx['categoria'] = categoria_menu
        return ctx

class articulo(DetailView):
    model = Noticia
    template_name = 'noticias/articulo.html'
=======
>>>>>>> 70dda3e4ca0ff21c9524a9a5e8993a7a407678a4

def categoria(request, cat):
    cat_object = Categoria.objects.get(pk=cat)
    noticias_categoria = Noticia.objects.filter(categoria= cat)
    return render(request, 'noticias/categoria.html',{'nombre': cat_object.nombre,'noticias_cat': noticias_categoria})
<<<<<<< HEAD

def mision(request):
    return render(request, 'noticias/mision.html')

def somos(request):
    return render(request, 'noticias/somos.html')   
    
>>>>>>> Jorge
=======
    
    
>>>>>>> 70dda3e4ca0ff21c9524a9a5e8993a7a407678a4
