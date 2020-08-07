from django.db import models

#from .rut import verifica_rut

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
# eleccion_nacionalidad = [ 'Chilena', 'Argentina','Venezolana','Colombiana','Peruana','Boliviana',]
class Propietario(models.Model):
    #idPersona=models.CharField('Rut',max_length=10,primary_key=True, validators=[verifica_rut])
    idPersona=models.CharField('Rut',max_length=10,primary_key=True, help_text="Entre RUT en formato 99999999-X")
    sexo=models.CharField(max_length=1, choices=eleccion_sexo)
    nombres=models.CharField(max_length=45)
    apellido_Paterno=models.CharField(max_length=45)
    apellido_Materno=models.CharField(max_length=45)
    telefono=models.IntegerField()
    correo=models.EmailField()
    nacionalidad=models.CharField(max_length=45)
    fecha_Nacimiento=models.DateField(blank=True, null=True)

    def  __str__(self):
        nombreProp=self.nombres+" "+ self.apellido_Paterno
        return (nombreProp)

#    def  __str__(self):
#        return (self.nombres, self.apellido_Paterno,self.apellido_Materno,self.fecha_Nacimiento,)

class Perfil(models.Model):
    idPerfil=models.IntegerField(unique=True)
    descripcion=models.CharField(max_length=255)
    nivel=models.IntegerField()

class Usuario(models.Model):
    idUsuario=models.CharField('Rut Usuario',max_length=10,help_text="Entre RUT en formato 99999999-X")
    #idPerfil=models.ForeignKey('Perfil',on_delete=models.CASCADE)
    id_Propietario=models.ForeignKey('Propietario',on_delete=models.CASCADE)
    idVivienda=models.ForeignKey('Vivienda',on_delete=models.CASCADE)
    nombres=models.CharField(max_length=45)
    apellido_Paterno=models.CharField(max_length=45)
    telefono=models.IntegerField()
    correo=models.EmailField()
    nacionalidad=models.CharField(max_length=45)
    # idCondominio=models.ForeignKey('Condominio',on_delete=models.CASCADE)
    estado_Usuario=models.BooleanField()
    contrasenia=models.CharField('Contraseña',max_length=100)
    fecha_Creacion=models.DateField(auto_now_add=True)
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(null=True,blank=True)

    def  __str__(self):
        nombreUsuario=self.nombres+"  "+ self.apellido_Paterno
        return (nombreUsuario)

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
    codigo_Referencia=models.IntegerField(blank=True, null=True)
    descripcion=models.CharField(max_length=255,blank=True, null=True)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(blank=True, null=True)



#       TABLAS SECCION 4

class CategoriaGastoComun(models.Model):
    idCategoria=models.IntegerField(unique=True)
    Descripcion_Categoria=models.CharField(max_length=255)

    def  __str__(self):
        Desc_Categoria=self.Descripcion_Categoria
        return (Desc_Categoria)

class SubcategoriaGastoComun(models.Model):
    idSubcategoria=models.IntegerField(unique=True)
    idCategoria=models.ForeignKey('CategoriaGastoComun',on_delete=models.CASCADE)
    Descripcion_Subcategoria=models.CharField(max_length=255)

    def  __str__(self):
        Desc_SubCategoria=self.Descripcion_Subcategoria
        return (Desc_SubCategoria)

class Calendario(models.Model):
    idCalendario=models.IntegerField(unique=True)
    mes=models.CharField(max_length=11)
    ano=models.IntegerField()

    def  __str__(self):
        Desc_Calendario=self.mes+' '+str(self.ano)
        return (Desc_Calendario)

class GastoComun(models.Model):
    idGastoComun=models.IntegerField(unique=True)
    idCalendario=models.ForeignKey('Calendario',on_delete=models.CASCADE )
    idSubCategoria=models.ForeignKey('SubCategoriaGastoComun',on_delete=models.CASCADE)
    #idCondominio=models.ForeignKey('Condominio',on_delete=models.CASCADE )
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
    cuotanumero=models.IntegerField(blank=True, null=True)
    totalcuotas=models.IntegerField(blank=True, null=True)
    tipoOperacion=models.CharField(max_length=1,blank=True, null=True)
    monto=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    fecha_Creacion=models.DateField(null=True)
    fecha_Modificacion=models.DateField(null=True)
    fecha_Eliminacion=models.DateField(blank=True, null=True)

eleccion_documento = [
    ('F', 'Factura'),
    ('B', 'Boleta'),
    ('H', 'Boleta Honorarios'),
    ('CC', 'Comprobante Caja Chica'),
    ('CT', 'Comprobante Transferencia'),
    ('CT', 'Comprobante Depósito'),
    ('CT', 'Comprobante Pago en Efectivo'),
    ]

class Documento(models.Model):
    idDocumento=models.IntegerField()
    tipoDoc=models.CharField(max_length=10,choices=eleccion_documento)
    numerodoc=models.IntegerField()
    montoTotal=models.IntegerField()
    fecha_Vencimiento=models.DateField(null=True)
    idCalendario=models.ForeignKey('Calendario',on_delete=models.CASCADE)
    observacion=models.CharField(max_length=255)
    fecha_Emision=models.DateField(null=True)
    fecha_Creacion=models.DateField(auto_now_add=True)


    def  __str__(self):
        nombredoc=self.tipoDoc
        return (nombredoc)

class DetalleDocumento(models.Model):
    idDetalleDocumento=models.IntegerField(unique=True)
    idDocumento=models.ForeignKey('Documento',on_delete=models.CASCADE )
    idDetalleGastoComun=models.ForeignKey('DetalleGastoComun',on_delete=models.CASCADE )


#       TABLAS SECCION 5

class Vivienda(models.Model):
    idVivienda=models.IntegerField(unique=True)
    #idCondominio=models.ForeignKey('Condominio',on_delete=models.CASCADE)
    codigoVivienda=models.CharField(max_length=12)
    piso=models.IntegerField()
    torre=models.CharField(max_length=1)

    def  __str__(self):
        nombreProp="Torre "+self.torre+" - Dp."+ str(self.idVivienda)
        return (nombreProp)

class ViviendaUsuario(models.Model):
    idUsuario=models.ForeignKey('Usuario',on_delete=models.CASCADE)
    idVivienda=models.ForeignKey('Vivienda',on_delete=models.CASCADE)
    observacion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(blank=True, null=True)

class CuentaVivienda(models.Model):
    idCuentaVivienda=models.IntegerField(unique=True)
    idVivienda=models.ForeignKey('Vivienda',on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=255)
    saldo=models.IntegerField()
    factor_Alicuota=models.FloatField()
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(blank=True, null=True)

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
    fecha_Eliminacion=models.DateField(blank=True, null=True)

class GastoComunCuentaVivienda(models.Model):
    idCalendario=models.ForeignKey('Calendario',on_delete=models.CASCADE)
    idCuentaVivienda=models.ForeignKey('CuentaVivienda',on_delete=models.CASCADE )
    monto=models.IntegerField()
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(blank=True, null=True)

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
    fecha_Eliminacion=models.DateField(blank=True, null=True)




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
    fecha_Eliminacion=models.DateField(blank=True, null=True)

class Producto(models.Model):
    idProducto=models.IntegerField()
    idProveedor=models.ForeignKey('Proveedor',on_delete=models.CASCADE )
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    descripcion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(blank=True, null=True)


class DetalleExistencia(models.Model):
    idDetalleExistencia=models.IntegerField(unique=True)
    idProducto=models.ForeignKey('Producto',on_delete=models.CASCADE )
    unidades=models.IntegerField()
    precio=models.IntegerField()
    observacion=models.CharField(max_length=255)
    fecha_Creacion=models.DateField()
    fecha_Modificacion=models.DateField()
    fecha_Eliminacion=models.DateField(blank=True, null=True)
