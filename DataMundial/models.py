from django.db import models

# Create your models here.


class selecciones(models.Model):
    seleccion = models.CharField(max_length=20)
    jug_nombre = models.CharField(max_length=20)
    jug_apellido = models.CharField(max_length=20)
    posicion = models.CharField(max_length=20)

class grupo(models.Model):
    letra = models.CharField(max_length=1)
    seleccion = models.CharField(max_length=40)

