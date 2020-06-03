from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField( max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
    telefono=models.CharField(max_length=9, verbose_name='celular')

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
