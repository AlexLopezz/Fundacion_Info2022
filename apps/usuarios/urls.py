from django.urls import path
from .views import Home, registroUser

urlpatterns = [
    path('', Home, name='home'),
    path('registro/', registroUser, name='registro'),
]