class Departamento(models.Model):
    iddepartamento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")

    class Meta:
        db_table = 'departamento'
    def __str__(self):
        return self.descripcion

class Estado(models.Model):
    idestado = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=8, verbose_name="Descripción")

    class Meta:
        db_table = 'estado'
    def __str__(self):
        return self.estado

class Grados(models.Model):
    idgrados = models.IntegerField(primary_key=True)
    descgrado = models.CharField(max_length=100, verbose_name="Descripción")

    class Meta:
        db_table = 'grados'
    def __str__(self):
        return self.descgrado

class Identificacion(models.Model):
    nombreapellido = models.CharField(max_length=400, verbose_name="Nombre - Apellido")
    codigofun = models.CharField(unique=True, max_length=10,verbose_name="Código Funcionnario")
    cua = models.CharField(unique=True, max_length=10,verbose_name="Código C.U.A.")
    departamento = models.ForeignKey('departamento',on_delete=models.CASCADE, db_column="descripcion", verbose_name="Departamento")
    grado = models.ForeignKey('grados', on_delete=models.CASCADE, db_column="descgrado", verbose_name="Grado")
    estado = models.ForeignKey('estado', on_delete=models.CASCADE, db_column="estado", verbose_name="Estado")

    class Meta:
        db_table = 'Identificacion'
    def __str__(self):
        return '%s %s %s' % (self.nombreapellido, self.codigofun, self.cua)