from django.shortcuts import render
from apps.noticias.models import Noticia 

def Home(request):
	noticias = Noticia.objects.all()
	return render(request,'home.html', {'noticias':noticias})