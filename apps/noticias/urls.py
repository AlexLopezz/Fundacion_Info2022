from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from .views import noticias, articulo
=======
from .views import noticias, articulo, categoria, mision, somos
>>>>>>> Jorge
=======
from .views import noticias, articulo, categoria
>>>>>>> 70dda3e4ca0ff21c9524a9a5e8993a7a407678a4

urlpatterns = [
    path('noticias/', noticias.as_view(), name='noticias'),
    path('articulo/<int:pk>',articulo.as_view(), name= 'articulo'),
<<<<<<< HEAD
<<<<<<< HEAD
=======
    path('categoria/<str:cat>', categoria, name ='categoria'),
    path('mision/', mision, name = 'mision'),
    path('somos/', somos, name = 'somos'),
>>>>>>> Jorge
=======
    path('categoria/<str:cat>', categoria, name ='categoria'),
>>>>>>> 70dda3e4ca0ff21c9524a9a5e8993a7a407678a4
]