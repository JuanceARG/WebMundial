from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class selecciones(models.Model):
    seleccion = models.CharField(max_length=20)
    jug_nombre = models.CharField(max_length=20)
    jug_apellido = models.CharField(max_length=20)
    posicion = models.CharField(max_length=20)

class grupo(models.Model):
    letra = models.CharField(max_length=1)
    seleccion = models.CharField(max_length=40)

class Registro(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to= 'avatares', null = True, blank = True)