from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registroUsuario(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    ctx = {'form' : form}

    return render(request, 'registration/registro.html', ctx)