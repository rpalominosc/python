# Generated by Django 3.0.6 on 2020-06-23 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0009_auto_20200623_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriagastocomun',
            old_name='DescripciónCategoria',
            new_name='Descripción_Categoria',
        ),
        migrations.RenameField(
            model_name='cuentacondominio',
            old_name='bancoEmisor',
            new_name='banco_Emisor',
        ),
        migrations.RenameField(
            model_name='cuentacondominio',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='cuentacondominio',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='cuentacondominio',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='cuentacondominio',
            old_name='numeroCuenta',
            new_name='numero_Cuenta',
        ),
        migrations.RenameField(
            model_name='cuentacondominio',
            old_name='razonSocial',
            new_name='razon_Social',
        ),
        migrations.RenameField(
            model_name='cuentavivienda',
            old_name='factorAlicuota',
            new_name='factor_Alicuota',
        ),
        migrations.RenameField(
            model_name='cuentavivienda',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='cuentavivienda',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='cuentavivienda',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='detallecuentacondominio',
            old_name='codigoReferencia',
            new_name='codigo_Referencia',
        ),
        migrations.RenameField(
            model_name='detallecuentacondominio',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='detallecuentacondominio',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='detallecuentacondominio',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='detalleexistencia',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='detalleexistencia',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='detalleexistencia',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='detalleexistencia',
            old_name='preico',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='detallegastocomun',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='detallegastocomun',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='detallegastocomun',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='documento',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='documento',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='gastocomun',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='gastocomun',
            old_name='fechaInicioCancelacion',
            new_name='fecha_InicioCancelacion',
        ),
        migrations.RenameField(
            model_name='gastocomun',
            old_name='fechaLimiteCancelación',
            new_name='fecha_LimiteCancelación',
        ),
        migrations.RenameField(
            model_name='gastocomun',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='gastocomuncuentavivienda',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='gastocomuncuentavivienda',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='gastocomuncuentavivienda',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='interes',
            old_name='fechaVigenciaDesde',
            new_name='fecha_VigenciaDesde',
        ),
        migrations.RenameField(
            model_name='interes',
            old_name='fechaVigenciaHasta',
            new_name='fecha_VigenciaHasta',
        ),
        migrations.RenameField(
            model_name='interescuentavivienda',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='interescuentavivienda',
            old_name='fechaDesde',
            new_name='fecha_Desde',
        ),
        migrations.RenameField(
            model_name='interescuentavivienda',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='interescuentavivienda',
            old_name='fechaHasta',
            new_name='fecha_Hasta',
        ),
        migrations.RenameField(
            model_name='interescuentavivienda',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='fecharecepcion',
            new_name='fecha_recepcion',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='nombrePagador',
            new_name='nombre_Pagador',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='nombreReceptor',
            new_name='nombre_Receptor',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='numeroDocumento',
            new_name='numero_Documento',
        ),
        migrations.RenameField(
            model_name='pagocuentavivienda',
            old_name='numeroRecibo',
            new_name='numero_Recibo',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='apellidoMaterno',
            new_name='apellido_Materno',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='apellidoPaterno',
            new_name='apellido_Paterno',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='razonSocial',
            new_name='razon_Social',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='telefonoMovil',
            new_name='telefono_Movil',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='telefonoMovil2',
            new_name='telefono_Movil2',
        ),
        migrations.RenameField(
            model_name='subcategoriagastocomun',
            old_name='DescripciónSubcategoria',
            new_name='Descripción_Subcategoria',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='estadoUsuario',
            new_name='estado_Usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='viviendausuario',
            old_name='fechaCreacion',
            new_name='fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='viviendausuario',
            old_name='fechaEliminacion',
            new_name='fecha_Eliminacion',
        ),
        migrations.RenameField(
            model_name='viviendausuario',
            old_name='fechaModificacion',
            new_name='fecha_Modificacion',
        ),
        migrations.RenameField(
            model_name='viviendausuario',
            old_name='ovservacion',
            new_name='observacion',
        ),
    ]
