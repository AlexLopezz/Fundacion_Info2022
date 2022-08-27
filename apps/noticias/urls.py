from django.urls import path

from .views import noticias, articulo, categoria,eventos



urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('categoria/<int:cat>', categoria, name ='categoria'),

    path('eventos/', eventos, name ='eventos'),

]