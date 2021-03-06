# Generated by Django 3.0.6 on 2020-06-24 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0019_usuario_idvivienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastocomun',
            name='idSubCategoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='condominio.SubcategoriaGastoComun'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategoriagastocomun',
            name='idCategoria',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='condominio.CategoriaGastoComun'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendario',
            name='mes',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='detallecuentacondominio',
            name='codigo_Referencia',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallecuentacondominio',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
