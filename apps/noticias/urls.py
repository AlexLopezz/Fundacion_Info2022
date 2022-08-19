from django.urls import path
<<<<<<< HEAD
from .views import noticias, articulo
=======
from .views import noticias, articulo, categoria, mision, somos
>>>>>>> Jorge

urlpatterns = [
    path('noticias/', noticias.as_view(), name='noticias'),
    path('articulo/<int:pk>',articulo.as_view(), name= 'articulo'),
<<<<<<< HEAD
=======
    path('categoria/<str:cat>', categoria, name ='categoria'),
    path('mision/', mision, name = 'mision'),
    path('somos/', somos, name = 'somos'),
>>>>>>> Jorge
]