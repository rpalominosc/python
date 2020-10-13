# Generated by Django 3.0.6 on 2020-06-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0017_auto_20200623_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentavivienda',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallecuentacondominio',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detalleexistencia',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallegastocomun',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='gastocomuncuentavivienda',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interescuentavivienda',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pagocuentavivienda',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='fecha_Nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='viviendausuario',
            name='fecha_Eliminacion',
            field=models.DateField(blank=True, null=True),
        ),
    ]