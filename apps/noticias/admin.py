from django.contrib import admin
from .models import Categoria, Noticia, Comentario, Evento

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Evento)
