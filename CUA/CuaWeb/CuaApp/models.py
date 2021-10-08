from django.db import models

# Create your models here.
class Identificacion(models.Model):
    nombreapellido = models.CharField(max_length=400,help_text="Ingrese APELLIDOS + NOMBRES")
    codigofun = models.CharField(unique=True, max_length=10, verbose_name="Cod.Funcionario")
    cua = models.CharField(unique=True, max_length=10)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING,default=None)
    grado = models.ForeignKey('Grados', models.DO_NOTHING, db_column='grado')
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'identificacion'
        verbose_name = "Identificación"
        verbose_name_plural = "Identificaciones"

    def __str__(self):
        return  '%s %s %s %s %s' % (self.id, self.nombreapellido, self.departamento, self.grado,self.estado)
        #return self.nombreapellido


class Departamento(models.Model):
    #id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        #managed = False
        db_table = 'departamento'

    def __str__(self):
        
        return self.descripcion

class Estado(models.Model):
    estado = models.CharField(max_length=8, verbose_name="Descripción")

    class Meta:
        db_table = 'estado'
    def __str__(self):
        return self.estado

class Grados(models.Model):
    descgrado = models.CharField(max_length=100, verbose_name="Descripción")

    class Meta:
        ordering = ['id']
        db_table = 'grados'
        verbose_name = "grado"
        verbose_name_plural = "grados"

    def __str__(self):
        #return self.descgrado
        return  self.descgrado