from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1: forms.Field(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.Field(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
