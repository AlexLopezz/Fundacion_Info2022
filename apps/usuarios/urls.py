from django.urls import path
from .views import registroUsuario

urlpatterns = [
    path('registro/', registroUsuario, name='registro'),
]