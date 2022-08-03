from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def Home(request):
    MUESTRA = '<html> <body> <h1> PROYECTO GRUPO 1. BOTELLAS DE AMOR </h1> </body> </html>'
    return HttpResponse(request)
# Create your views here.
