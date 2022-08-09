from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def Home(request):
    MUESTRA = '<html> <body> <h1> PROYECTO GRUPO 1. BOTELLAS DE AMOR </h1> </body> </html>'
    return HttpResponse(request)
# Create your views here.


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            message.success(request, f'Usuario {username} creado')
    else:
        form = UserCreationForm()
    
    context = {'form' : form}
    return render(request, 'registro.html')