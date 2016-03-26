# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True, null=True, blank=True)),
                ('manufacturer', models.CharField(max_length=100, null=True, blank=True)),
                ('type_cereal', models.CharField(max_length=1, null=True, blank=True)),
                ('calories', models.IntegerField(null=True, blank=True)),
                ('protein', models.IntegerField(null=True, blank=True)),
                ('Fat', models.IntegerField(null=True, blank=True)),
                ('sodium', models.IntegerField(null=True, blank=True)),
                ('dietary_fiber', models.FloatField(null=True, blank=True)),
                ('carbs', models.FloatField(null=True, blank=True)),
                ('sugars', models.IntegerField(null=True, blank=True)),
                ('display_shelf', models.IntegerField(null=True, blank=True)),
                ('potassium', models.IntegerField(null=True, blank=True)),
                ('vit_min', models.IntegerField(null=True, blank=True)),
                ('serving_size_weight', models.FloatField(null=True, blank=True)),
                ('cups_per_serving', models.FloatField(null=True, blank=True)),
            ],
        ),
    ]
