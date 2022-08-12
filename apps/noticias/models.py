from pyexpat import model
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50, null = True, blank= True)

    def __str__(self) -> str:
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50, null = True, blank=True)
    fechaCreacion = models.DateField(auto_now_add=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to= 'noticias', null=True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, null=True, blank= True)

    def __str__(self) -> str:
        return self.titulo


