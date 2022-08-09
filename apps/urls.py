from django.urls import path
from .views import Home, registro
from . import views

urlpatterns = [
    path('', Home, name="home"),
    path('register/', registro, name= 'registro'),
]