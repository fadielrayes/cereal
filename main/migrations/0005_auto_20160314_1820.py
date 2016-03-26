# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160314_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='main.Manufacturer', null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='name',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
    ]
