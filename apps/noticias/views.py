import random
from re import template
from django.shortcuts import render
<<<<<<< HEAD

from django.db.models import Q
from django.views.generic import DetailView

=======
from django.views.generic import ListView
>>>>>>> 19e433d1f53521f03d824a8fdee8f16bccb633ea
from apps.noticias.models import Categoria, Comentario, Noticia 
from django.contrib.auth import get_user_model
from .forms import FormComentario
# Create your views here.

User = get_user_model()

def noticias(request):
    todasNoticias = Noticia.objects.all() #Devuelve una lista.
    todasCategorias = Categoria.objects.all() #Devuelve una lista.
    try:
        noticiasRandom = random.sample(list(todasNoticias), 5)
    except:
        noticiasRandom = None
        
    ctx={
        'noticias': todasNoticias, 
        'categorias': todasCategorias,
        'randomNoticias': noticiasRandom,
    }
    return render(request, 'noticias/seccion_noticias.html', ctx)

def articulo(request, art):
    articuloSeleccionado = Noticia.objects.get(pk=art) #Aqui obtengo el objeto articuloSeleccionado.
    comentarios = Comentario.objects.filter(noticia_Comentario_id=art)
    
    if request.method == 'POST':
        formComentario = FormComentario(request.POST)
        if formComentario.is_valid():
            contenido= request.POST.get('contenido')
            Comentario.objects.create(noticia_Comentario_id=art, nombre=request.user, contenido=contenido)
    else:
        formComentario= FormComentario()

    ctx={
        'noticia': articuloSeleccionado,
        'comentarios': comentarios,
        'formComentario': formComentario,
    }
    return render(request, 'noticias/articulo.html', ctx)

def categoria(request, cat):
    cat_object = Categoria.objects.get(pk=cat)
    noticias_categoria = Noticia.objects.filter(categoria= cat)
<<<<<<< HEAD
    return render(request, 'noticias/categoria.html',{'nombre': cat_object.nombre,'noticias_cat': noticias_categoria})



def buscarNoticias(request):
    busqueda = request.GET.get('buscar')
    noticias = Noticia.objects.all()

    if busqueda:
        noticias = Noticia.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(autor__icontains = busqueda) |
            Q(fechaCreacion__icontains = busqueda) |
            Q(contenido__icontains = busqueda) |
            Q(categoria__icontains = busqueda)
        ).distinct()

    return render(request, 'noticias/seccion_noticias.html', {'noticias': noticias})
=======
    return render(request, 'noticias/filtro/categoria.html',{'nombre': cat_object.nombre,'noticias_cat': noticias_categoria})
>>>>>>> 19e433d1f53521f03d824a8fdee8f16bccb633ea

def noticiasRecientes(request):
    noticias = Noticia.objects.all().order_by('-fechaCreacion') #Ordenamiento ascendente-descendente
    return render(request, 'noticias/filtro/reciente.html',{'noticias':noticias})

def noticiasAntiguas(request):
    noticias = Noticia.objects.all().order_by('fechaCreacion') #Ordenamiento descendente-ascendente
    return render(request,'noticias/filtro/antiguo.html',{'noticias': noticias})


def eventos(request):
    return render(request, 'eventos/eventos.html')

