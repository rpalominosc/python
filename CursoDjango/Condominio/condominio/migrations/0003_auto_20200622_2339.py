# Generated by Django 3.0.6 on 2020-06-22 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0002_cuentacondominio_detallecuentacondominio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCalendario', models.IntegerField(unique=True)),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaGastoComun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategoria', models.IntegerField(unique=True)),
                ('DescripciónCategoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCuentaVivienda', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('saldo', models.IntegerField()),
                ('factorAlicuota', models.FloatField()),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDocumento', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=1000)),
                ('observacion', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='medioPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idmediopago', models.IntegerField(unique=True)),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProveedor', models.IntegerField()),
                ('razonSocial', models.CharField(max_length=255)),
                ('giro', models.CharField(max_length=255)),
                ('telefonoMovil', models.CharField(max_length=9)),
                ('telefonoMovil2', models.CharField(max_length=9)),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SubcategoriaGastoComun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idSubcategoria', models.IntegerField(unique=True)),
                ('DescripciónSubcategoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idVivienda', models.IntegerField(unique=True)),
                ('codigoVivienda', models.CharField(max_length=10)),
                ('piso', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('idCondominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Condominio')),
            ],
        ),
        migrations.RenameField(
            model_name='cuentacondominio',
            old_name='fechaEliminación',
            new_name='fechaEliminacion',
        ),
        migrations.RenameField(
            model_name='detallecuentacondominio',
            old_name='fechaEliminación',
            new_name='fechaEliminacion',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='fechaEliminación',
            new_name='fechaEliminacion',
        ),
        migrations.CreateModel(
            name='ViviendaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ovservacion', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Usuario')),
                ('idVivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Vivienda')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProducto', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
                ('idProveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='PagoCuentaVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPago', models.IntegerField(unique=True)),
                ('numeroDocumento', models.CharField(max_length=100)),
                ('nombreReceptor', models.CharField(max_length=100)),
                ('nombrePagador', models.CharField(max_length=100)),
                ('fecharecepcion', models.DateField()),
                ('numeroRecibo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('monto', models.IntegerField()),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
                ('idCalendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Calendario')),
                ('idCuentaVivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.CuentaVivienda')),
                ('idmediopago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.medioPago')),
            ],
        ),
        migrations.CreateModel(
            name='InteresCuentaVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idInteres', models.IntegerField(unique=True)),
                ('fechaDesde', models.DateField()),
                ('fechaHasta', models.DateField()),
                ('monto', models.IntegerField()),
                ('factorInteres', models.FloatField()),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
                ('idCalendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Calendario')),
                ('idCuentaVivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.CuentaVivienda')),
            ],
        ),
        migrations.CreateModel(
            name='GastoComunCuentaVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
                ('idCalendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Calendario')),
                ('idCuentaVivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.CuentaVivienda')),
            ],
        ),
        migrations.CreateModel(
            name='GastoComun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idGastoComun', models.IntegerField(unique=True)),
                ('estado', models.BooleanField()),
                ('montoTotal', models.IntegerField()),
                ('fechaInicioCancelacion', models.DateField()),
                ('fechaLimiteCancelación', models.DateField()),
                ('observacion', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('idCalendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Calendario')),
                ('idCondominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Condominio')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleGastoComun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDetalleGastoComun', models.IntegerField(unique=True)),
                ('cuotanumero', models.IntegerField()),
                ('totalcuotas', models.IntegerField()),
                ('tipoOperacion', models.CharField(max_length=1)),
                ('monto', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.CategoriaGastoComun')),
                ('idGastoComun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.GastoComun')),
                ('idSubCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.SubcategoriaGastoComun')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleExistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDetalleExistencia', models.IntegerField(unique=True)),
                ('unidades', models.IntegerField()),
                ('preico', models.IntegerField()),
                ('observacion', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateField()),
                ('fechaModificacion', models.DateField()),
                ('fechaEliminacion', models.DateField()),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDetalleDocumento', models.IntegerField(unique=True)),
                ('idDetalleGastoComun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.DetalleGastoComun')),
                ('idDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Documento')),
            ],
        ),
        migrations.AddField(
            model_name='cuentavivienda',
            name='idVivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condominio.Vivienda'),
        ),
    ]
