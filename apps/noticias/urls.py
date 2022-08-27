from django.urls import path
<<<<<<< HEAD

from .views import noticias, articulo, categoria, eventos
=======
from .views import noticias, articulo, categoria, NoticiasAntiguas
>>>>>>> 8bdaf1d4191be79b6bec70ae101f72f1aad08741


urlpatterns = [
    path('noticias/', noticias, name='noticias'),
    path('articulo/<int:art>',articulo, name= 'articulo'),
    path('categoria/<int:cat>', categoria, name ='categoria'),
<<<<<<< HEAD
    path('eventos/', eventos, name="evento"),
=======
    path('noticias/antiguas', NoticiasAntiguas.as_view(), name='antiguas'),
>>>>>>> 8bdaf1d4191be79b6bec70ae101f72f1aad08741
]