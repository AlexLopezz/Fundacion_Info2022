from django.shortcuts import render

def home(request):
	return render(request,'home.html')

def sobre_nosotros(request):
    return render(request, 'sobre-nosotros.html')
