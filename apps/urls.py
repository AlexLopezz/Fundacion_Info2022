from django.urls import path
from .views import Home, registro

urlpatterns = [
    path('', Home, name="home"),
    path('register/', registro, name= 'registro'),
]