from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


def Home(request):
    return render(request, 'apps/home.html')
# Create your views here.

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return redirect(to='home')
    else:
        form = UserRegisterForm()
    ctx = {'form' : form}

    return render(request, 'registration/registro.html', ctx)