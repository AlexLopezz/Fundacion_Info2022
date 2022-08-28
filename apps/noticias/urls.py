from django.urls import path

<<<<<<< HEAD
from .views import noticias, articulo, categoria,eventos
=======
from .views import noticias, articulo, categoria, eventos
>>>>>>> matias



urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
<<<<<<< HEAD

    path('eventos/', eventos, name ='eventos'),
=======
    path('eventos/', eventos, name="evento"),
>>>>>>> matias

]