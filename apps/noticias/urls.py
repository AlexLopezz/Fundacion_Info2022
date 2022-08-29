from django.urls import path
from .views import noticias, articulo, categoria, Eventos, noticiasAntiguas, noticiasRecientes



urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
    path('eventos/', Eventos.as_view(), name="evento"),
    path('noticias/antiguas', noticiasAntiguas, name='antiguas'),
    path('noticias/recientes', noticiasRecientes, name='recientes'),
]