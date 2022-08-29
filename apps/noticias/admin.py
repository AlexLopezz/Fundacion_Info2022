from django.contrib import admin
from .models import Categoria, Noticia, Comentario, Evento, Modalidad

# Register your models here.
admin.site.register(Noticia)
admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Evento)
admin.site.register(Modalidad)

