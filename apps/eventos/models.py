from django.db import models

# Create your models here.
class Modalidad(models.Model):
    nombre = models.CharField(max_length=150)

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