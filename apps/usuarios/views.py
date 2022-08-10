from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def Home(request):
	return render(request,'usuarios/home.html')

# Create your views here.
def registroUser(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    data = {'form' : form}

    return render(request, 'registration/registro.html', data)