from django.urls import path
from .views import noticias, articulo, categoria, mision


urlpatterns = [
    path('noticias/', noticias.as_view(), name='noticias'),
    path('articulo/<int:pk>',articulo.as_view(), name= 'articulo'),
    path('mision/', mision, name= 'mision'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
]