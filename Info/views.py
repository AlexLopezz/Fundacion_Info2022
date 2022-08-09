from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def Home(request):
	return render(request,'home.html')