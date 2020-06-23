from django.db import models

# Create your models here.

#       TABLAS SECCION 1

class Condominio(models.Model):
    idCondominio=models.IntegerField(primary_key=True)
    razonSocial=models.CharField(max_length=200)
    rut=models.IntegerField(default=11111111)
    giro=models.CharField(max_length=200)
    telefonoRedFija=models.CharField(max_length=20)
    telefonoMovil=models.CharField(max_length=20)
    correo=models.EmailField()
    direccion=models.CharField(max_length=255)
    class Meta:
        verbose_name = "condominio"
        verbose_name_plural = "condominios"

    def  __str__(self):
        return (self.razonSocial)

class Interes(models.Model):
    idInteres=models.IntegerField(primary_key=True)
    idCondominio=models.ForeignKey('Condominio', on_delete=models.CASCADE)
    factorInteres=models.FloatField()
    fecha_VigenciaDesde=models.DateField()
    fecha_VigenciaHasta=models.DateField()

#       TABLAS SECCION 2
eleccion_sexo = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
    ]
class Persona(models.Model):
    idPersona=models.IntegerField(primary_key=True)
    sexo=models.CharField(max_length=1, choices=eleccion_sexo)
    nombres=models.CharField(max_length=45)
    apellido_Paterno=models.CharField(max_length=45)
    apellido_Materno=models.CharField(max_length=45)
    nacionalidad=models.CharField(max_length=45)
    fecha_Nacimiento=models.DateField()

#    def  __str__(self):
#        return (self.nombres, self.apellido_Paterno,self.apellido_Materno,self.fecha_Nacimiento,)

class Perfil(models.Model):
    idPerfil=models.IntegerField(unique=True)
    descripcion=models.CharField(max_length=255)
    nivel=models.IntegerField()

class Usuario(models.Model):
    idUsuario=models.IntegerField(unique=True)
    idPerfil=models.ForeignKey('Perfil',on_delete=models.CASCADE)
    idPersona=models.ForeignKey('Persona',on_delete=models.CASCADE)
    idCondominio=models.ForeignKey('Condominio',on_delete=models.CASCADE)
    estado_Usuario=models.BooleanField()
    contrasenia=models.CharField(max_length=100)
    fecha_Creacion=models.DateField(auto_now_add=True)
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()

#       TABLAS SECCION 3

class CuentaCondominio(models.Model):
    idCuentaCondominio=models.IntegerField(unique=True)
    idCondominio=models.ForeignKey('Condominio',on_delete=models.CASCADE)
    razon_Social=models.CharField(max_length=255)
    numero_Cuenta=models.CharField(max_length=255)
    banco_Emisor=models.CharField(max_length=255)
    observacion=models.CharField(max_length=255,blank=True, null=True)
    fecha_Creacion=models.DateField(auto_now_add=True)
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(blank=True, null=True)

class DetalleCuentaCondominio(models.Model):
    idTransaccion=models.IntegerField(unique=True)
    idCuentaCondominio=models.ForeignKey('CuentaCondominio',on_delete=models.CASCADE )
    fecha=models.DateField()
    asunto=models.IntegerField()
    monto=models.IntegerField()
    codigo_Referencia=models.IntegerField()
    descripcion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()



#       TABLAS SECCION 4

class CategoriaGastoComun(models.Model):
    idCategoria=models.IntegerField(unique=True)
    Descripción_Categoria=models.CharField(max_length=255)

class SubcategoriaGastoComun(models.Model):
    idSubcategoria=models.IntegerField(unique=True)
    Descripción_Subcategoria=models.CharField(max_length=255)

class Calendario(models.Model):
    idCalendario=models.IntegerField(unique=True)
    mes=models.IntegerField()
    ano=models.IntegerField()

class GastoComun(models.Model):
    idGastoComun=models.IntegerField(unique=True)
    idCalendario=models.ForeignKey('Calendario',on_delete=models.CASCADE )
    idCondominio=models.ForeignKey('Condominio',on_delete=models.CASCADE )
    estado=models.BooleanField()
    montoTotal=models.IntegerField()
    fecha_InicioCancelacion=models.DateField()
    fecha_LimiteCancelación=models.DateField()
    observacion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()

class DetalleGastoComun(models.Model):
    idDetalleGastoComun=models.IntegerField(unique=True)
    idGastoComun=models.ForeignKey('GastoComun',on_delete=models.CASCADE )
    idCategoria=models.ForeignKey('CategoriaGastoComun',on_delete=models.CASCADE )
    idSubCategoria=models.ForeignKey('SubcategoriaGastoComun',on_delete=models.CASCADE )
    cuotanumero=models.IntegerField()
    totalcuotas=models.IntegerField()
    tipoOperacion=models.CharField(max_length=1)
    monto=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()

class Documento(models.Model):
    idDocumento=models.IntegerField()
    ubicacion=models.CharField(max_length=1000)
    observacion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Eliminacion=models.DateField()

class DetalleDocumento(models.Model):
    idDetalleDocumento=models.IntegerField(unique=True)
    idDocumento=models.ForeignKey('Documento',on_delete=models.CASCADE )
    idDetalleGastoComun=models.ForeignKey('DetalleGastoComun',on_delete=models.CASCADE )


#       TABLAS SECCION 5

class Vivienda(models.Model):
    idVivienda=models.IntegerField(unique=True)
    idCondominio=models.ForeignKey('Condominio',on_delete=models.CASCADE)
    codigoVivienda=models.CharField(max_length=10)
    piso=models.IntegerField()
    numero=models.IntegerField()

class ViviendaUsuario(models.Model):
    idUsuario=models.ForeignKey('Usuario',on_delete=models.CASCADE)
    idVivienda=models.ForeignKey('Vivienda',on_delete=models.CASCADE)
    observacion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()

class CuentaVivienda(models.Model):
    idCuentaVivienda=models.IntegerField(unique=True)
    idVivienda=models.ForeignKey('Vivienda',on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=255)
    saldo=models.IntegerField()
    factor_Alicuota=models.FloatField()
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()

class medioPago(models.Model):
    idmediopago=models.IntegerField(unique=True)
    descripcion=models.CharField(max_length=255)

class PagoCuentaVivienda(models.Model):
    idPago=models.IntegerField(unique=True)
    idCalendario=models.ForeignKey('Calendario',on_delete=models.CASCADE )
    idCuentaVivienda=models.ForeignKey('CuentaVivienda',on_delete=models.CASCADE )
    idmediopago=models.ForeignKey('medioPago',on_delete=models.CASCADE )
    numero_Documento=models.CharField(max_length=100)
    nombre_Receptor=models.CharField(max_length=100)
    nombre_Pagador=models.CharField(max_length=100)
    fecha_recepcion=models.DateField()
    numero_Recibo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    monto=models.IntegerField()
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()

class GastoComunCuentaVivienda(models.Model):
    idCalendario=models.ForeignKey('Calendario',on_delete=models.CASCADE)
    idCuentaVivienda=models.ForeignKey('CuentaVivienda',on_delete=models.CASCADE )
    monto=models.IntegerField()
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()

class InteresCuentaVivienda(models.Model):
    idInteres=models.IntegerField(unique=True)
    idCalendario=models.ForeignKey('Calendario',on_delete=models.CASCADE)
    idCuentaVivienda=models.ForeignKey('CuentaVivienda',on_delete=models.CASCADE )
    fecha_Desde=models.DateField()
    fecha_Hasta=models.DateField()
    monto=models.IntegerField()
    factorInteres=models.FloatField()
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()




#       TABLAS SECCION 6

class Proveedor(models.Model):
    idProveedor=models.IntegerField()
    razon_Social=models.CharField(max_length=255)
    giro=models.CharField(max_length=255)
    telefono_Movil=models.CharField(max_length=9)
    telefono_Movil2=models.CharField(max_length=9)
    correo=models.EmailField()
    direccion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()

class Producto(models.Model):
    idProducto=models.IntegerField()
    idProveedor=models.ForeignKey('Proveedor',on_delete=models.CASCADE )
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()


class DetalleExistencia(models.Model):
    idDetalleExistencia=models.IntegerField(unique=True)
    idProducto=models.ForeignKey('Producto',on_delete=models.CASCADE )
    unidades=models.IntegerField()
    precio=models.IntegerField()
    observacion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField()
