from django.urls import path
<<<<<<< HEAD

from .views import noticias, articulo, categoria, buscarNoticias
=======
from .views import noticias, articulo, categoria
>>>>>>> 422acbca05208823ffb736e2070628af6b24f5cf


urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
    path('noticias/', buscarNoticias, name='buscarNoticias'),
]