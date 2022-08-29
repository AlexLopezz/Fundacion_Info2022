from django.urls import path
from .views import ListaEventos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('eventos/', ListaEventos.as_view(), name="evento"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)