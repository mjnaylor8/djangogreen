# Generated by Django 2.0.5 on 2018-07-30 20:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wards',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('unitid', models.IntegerField()),
                ('code', models.CharField(max_length=9)),
                ('hectares', models.DecimalField(decimal_places=3, max_digits=12)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
    ]
