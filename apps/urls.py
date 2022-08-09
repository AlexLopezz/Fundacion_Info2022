from django.urls import path
<<<<<<< HEAD:apps/urls.py
from .views import Home, registro

urlpatterns = [
    path('', Home, name="home"),
    path('register/', registro, name= 'registro'),
=======
from . import views

app_name = 'usuarios'


urlpatterns = [
    path('registro/', views.registro, name = 'registro')
>>>>>>> 6b26a3f5790fdd6b3c1d4d0f9077165d2ae4dc5e:apps/usuarios/urls.py
]