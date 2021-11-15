from django.db import models

# Create your models here.
class Identificacion(models.Model):
    managed = True
    nombreapellido = models.CharField(max_length=400,help_text="Ingrese APELLIDOS + NOMBRES",verbose_name="Nombre - Apellido",)
    codigofun = models.CharField(unique=True, max_length=10, verbose_name="Cod.Funcionario")
    cua = models.CharField(unique=True, max_length=10)
    grado = models.ForeignKey('Grados', models.DO_NOTHING, db_column='grado')
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', blank=True, null=True)
    departamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento')

    class Meta:
        #managed = False
        db_table = 'funcionario'
        verbose_name = "Identificación"
        verbose_name_plural = "Identificaciones"


    def __str__(self):
        return  "%s %s %s %s %s %s" % (self.nombreapellido, self.codigofun, self.cua, self.departamento,self.grado,self.estado)

      
class Departamento(models.Model):
    managed = True
    descripcion = models.CharField(max_length=100, verbose_name="Departamento")
    
    class Meta:
        ordering = ['id']
        db_table = 'departamento'
        verbose_name= 'departamento'
        verbose_name_plural= 'departamentos'
    def __str__(self):
        return self.descripcion
    
class Estado(models.Model):
    managed = True
    estado = models.CharField(max_length=8, verbose_name="Descripción")

    class Meta:
        db_table = 'estado'
    def __str__(self):
        return self.estado

class Grados(models.Model):
    managed = True
    descgrado = models.CharField(max_length=100, verbose_name="Descripción")

    class Meta:
        ordering = ['id']
        db_table = 'grados'
        verbose_name = "grado"
        verbose_name_plural = "grados"

    def __str__(self):
        return  self.descgrado