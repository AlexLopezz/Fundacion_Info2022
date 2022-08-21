from django.shortcuts import render

def home(request):
	return render(request,'home.html')

def mision(request):
    return render(request, 'mision.html')

def somos(request):
    return render(request, 'somos.html')