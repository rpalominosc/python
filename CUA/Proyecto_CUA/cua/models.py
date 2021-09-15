from django.db import models


# Create your models here.
class Departamento(models.Model):

    # id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'departamento'
    def __str__(self):
        return  '%s, %s' % (self.id,self.descripcion)


class Estado(models.Model):
    # id = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=8, verbose_name="Descripción")

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'estado'
    def __str__(self):
        return  '%s, %s' % (self.id,self.estado)


class Grados(models.Model):
    # id = models.IntegerField(primary_key=True)
    descgrado = models.CharField(max_length=100, verbose_name="DescripciOn")

    class Meta:
        managed = False
        ordering = ['id']
        db_table = 'grados'
    def __str__(self):
        return  '%s, %s' % (self.id,self.descgrado)

class Identificacion(models.Model):
    # id = models.IntegerField(primary_key=True)
    nombreapellido = models.CharField(max_length=400, verbose_name="Nombre - Apellido")
    codigofun = models.CharField(unique=True, max_length=10,verbose_name="Código Funcionnario")
    cua = models.CharField(unique=True, max_length=10,verbose_name="Código C.U.A.")
    departamento = models.ForeignKey('Departamento',models.DO_NOTHING)
    grado = models.ForeignKey('grados', models.DO_NOTHING, verbose_name="Grado")
    estado = models.ForeignKey('estado', models.DO_NOTHING, verbose_name="Estado")

    class Meta:
        managed = False
        db_table = 'Identificacion'
    #    list_display = ('nombreapellido', 'codigofun',)
    def __str__(self):
        return  self.nombreapellido #'%s %s %s' % (self.nombreapellido, self.codigofun, self.cua)