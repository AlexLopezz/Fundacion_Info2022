"""Info URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, sobre_nosotros
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('apps.usuarios.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('seccion/',include('apps.noticias.urls')),
    path('eventos/',include('apps.eventos.urls')),
    path('sobre-nosotros/', sobre_nosotros, name = 'sobre nosotros'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
