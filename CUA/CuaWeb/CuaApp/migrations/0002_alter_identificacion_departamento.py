# Generated by Django 3.2.8 on 2021-11-11 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CuaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identificacion',
            name='departamento',
            field=models.ForeignKey(db_column='departamento_id', on_delete=django.db.models.deletion.DO_NOTHING, to='CuaApp.departamento'),
        ),
    ]
