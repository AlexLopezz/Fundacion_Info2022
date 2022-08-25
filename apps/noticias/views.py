from django.shortcuts import render
from django.db.models import Q
from apps.noticias.models import Categoria, Comentario, Noticia 
from django.contrib.auth import get_user_model
from .forms import FormComentario
# Create your views here.

User = get_user_model()

def noticias(request):
    todasNoticas = Noticia.objects.all()
    todasCategorias = Categoria.objects.all()
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
            comentario= Comentario.objects.create(noticia_Comentario_id=art, nombre=request.user, contenido=contenido)
            comentario.save()
    else:
        formComentario= FormComentario()

    ctx={
        'noticia': articuloSeleccionado,
        'comentarios': comentarios,
        'formComentario': formComentario,
    }
    return render(request, 'noticias/articulo.html', ctx)



def sobre_nosotros(request):
    return render(request, 'noticias/sobre-nosotros.html')

def categoria(request, cat):
    cat_object = Categoria.objects.get(pk=cat)
    noticias_categoria = Noticia.objects.filter(categoria= cat)
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