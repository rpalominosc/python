# Generated by Django 3.0.6 on 2020-06-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=9, verbose_name='celular'),
        ),
    ]
