from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50, null = True, blank= True)

    def __str__(self):
        return self.nombre
<<<<<<< HEAD
=======
    
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50, null = True, blank=True)
    fechaCreacion = models.DateField(auto_now_add=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to= 'noticias', null=True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.titulo

class Comentario(models.Model):
    noticia_Comentario = models.ForeignKey(Noticia, related_name="comentario",on_delete=models.CASCADE)
    nombre = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_de_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre.username

class Modalidad(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=150)

class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    fechaInicio= models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)
    fechaFin= models.DateField('Fecha de finalizacion', auto_now= False, auto_now_add= False, null= True, blank=True)
    activo = models.BooleanField(default= True, verbose_name='Evento activo')
    modalidad= models.ForeignKey(Modalidad, on_delete=models.CASCADE, null= True, blank= True)



=======
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    lugar = models.CharField(max_length=150)
    contenido = models.CharField(max_length= 200)
    fechaInicio = models.DateField('Fecha de inicio', auto_now = False, auto_now_add= True)
    fechaFin = models.DateField('Fecha de finalizacion', auto_now= False, auto_now_add = False)
    modalidad = models.ForeignKey(Modalidad, on_delete= models.CASCADE, null = True, blank = True)
    gratuito = models.BooleanField(default = True, verbose_name= "Gratis")
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    def __str__(self):
        return self.nombre

    
>>>>>>> de9435e8f7b3699d0bdc622add34ae493c3b7aa4
