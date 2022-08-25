from django.urls import path
from .views import noticias, articulo, categoria, mision, buscarNoticias


urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('mision/', mision, name= 'mision'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
    path('noticias/', buscarNoticias, name='buscarNoticias'),
]