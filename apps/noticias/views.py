from django.shortcuts import render
from django.views.generic import DetailView

from apps.noticias.models import Categoria, Comentario, Noticia 
from django.contrib.auth import get_user_model
from .forms import FormComentario
# Create your views here.

User = get_user_model()

def noticias(request):
    todasNoticas = Noticia.objects.all() #Devuelve una lista.
    todasCategorias = Categoria.objects.all() #Devuelve una lista.
    ctx={
        'noticias': todasNoticas, 
        'categorias': todasCategorias,
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
    try:
        noticias_categoria = Noticia.objects.filter(categoria= cat)
    except:
        noticias_categoria = None
    return render(request, 'noticias/filtro/categoria.html',{'nombre': cat_object.nombre,'noticias_cat': noticias_categoria})

def noticiasRecientes(request):
    noticias = Noticia.objects.all().order_by('-fechaCreacion') #Ordenamiento ascendente-descendente
    return render(request, 'noticias/filtro/reciente.html',{'noticias':noticias})

def noticiasAntiguas(request):
    noticias = Noticia.objects.all().order_by('fechaCreacion') #Ordenamiento descendente-ascendente
    return render(request,'noticias/filtro/antiguo.html',{'noticias': noticias})

