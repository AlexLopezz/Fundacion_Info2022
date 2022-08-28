from django.urls import path
from .views import noticias, articulo, categoria, eventos, noticiasAntiguas, noticiasRecientes





urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('categoria/<int:cat>', categoria, name ='categoria'),

    path('eventos/', eventos, name="evento"),
<<<<<<< HEAD


=======
    path('noticias/antiguas', noticiasAntiguas, name='antiguas'),
    path('noticias/recientes', noticiasRecientes, name='recientes'),
>>>>>>> 19e433d1f53521f03d824a8fdee8f16bccb633ea
]