from django.urls import path
from .views import noticias, articulo
from .views import noticias, articulo, categoria, mision, somos
from .views import noticias, articulo, categoria

urlpatterns = [
    path('noticias/', noticias.as_view(), name='noticias'),
    path('articulo/<int:pk>',articulo.as_view(), name= 'articulo'),
<<<<<<< HEAD
    path('mision/', mision, name = 'mision'),
    path('somos/', somos, name = 'somos'),
    path('categoria/<str:cat>', categoria, name ='categoria'),
=======
    path('categoria/<int:cat>', categoria, name ='categoria'),
>>>>>>> alex
]