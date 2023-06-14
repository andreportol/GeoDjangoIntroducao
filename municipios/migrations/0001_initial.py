# Generated by Django 4.2.2 on 2023-06-12 18:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipios_MS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_mun', models.CharField(max_length=7)),
                ('nm_mun', models.CharField(max_length=50)),
                ('sigla_uf', models.CharField(max_length=2)),
                ('area_km2', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674)),
            ],
        ),
    ]