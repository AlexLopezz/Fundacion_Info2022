from django.shortcuts import render

def Home(request):
	return render(request,'home.html')

def mision(request):
    return render(request, 'mision.html')
