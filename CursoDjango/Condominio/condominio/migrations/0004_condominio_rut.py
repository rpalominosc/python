# Generated by Django 3.0.6 on 2020-06-23 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0003_auto_20200622_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='rut',
            field=models.IntegerField(default=None),
        ),
    ]
