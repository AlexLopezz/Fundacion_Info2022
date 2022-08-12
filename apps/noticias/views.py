from django.shortcuts import render
from apps.noticias.models import Noticia 
# Create your views here.

def noticias(request):
    TodasNoticias = Noticia.objects.all()
    return render(request,'noticias/seccion_noticias.html',{'noticias':TodasNoticias})