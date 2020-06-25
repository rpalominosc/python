# Generated by Django 3.0.6 on 2020-06-25 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0021_auto_20200624_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='fecha_Eliminacion',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='documento',
            name='fecha_Emision',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='fecha_Vencimiento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='idCalendario',
            field=models.ForeignKey(default=11111, on_delete=django.db.models.deletion.CASCADE, to='condominio.Calendario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documento',
            name='montoTotal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documento',
            name='numerodoc',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documento',
            name='tipoDoc',
            field=models.CharField(choices=[('F', 'Factura'), ('B', 'Boleta'), ('H', 'Boleta Honorarios'), ('C', 'Comprobante Caja Chica')], default='F', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallegastocomun',
            name='cuotanumero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallegastocomun',
            name='fecha_Creacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='detallegastocomun',
            name='fecha_Modificacion',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='detallegastocomun',
            name='tipoOperacion',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='detallegastocomun',
            name='totalcuotas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='fecha_Creacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
