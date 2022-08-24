from django.urls import path
from .views import noticias, articulo, categoria, sobre_nosotros


urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('sobre-nosotros/', sobre_nosotros, name= 'sobre nosotros'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
]