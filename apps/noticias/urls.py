from django.urls import path
<<<<<<< HEAD
from .views import noticias, articulo, categoria, mision, buscarNoticias
=======
from .views import noticias, articulo, categoria, sobre_nosotros
>>>>>>> 3d45279f2603d896b495b4a8db1cefcb3ab0f4fd


urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('sobre-nosotros/', sobre_nosotros, name= 'sobre nosotros'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
    path('noticias/', buscarNoticias, name='buscarNoticias'),
]