# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='type_cereal',
            new_name='cereal_type',
        ),
        migrations.RenameField(
            model_name='cereal',
            old_name='manufacturer',
            new_name='manufacturer_for_cereal',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='Fat',
        ),
        migrations.RemoveField(
            model_name='cereal',
            name='name',
        ),
        migrations.AddField(
            model_name='cereal',
            name='fat',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='name_of_cereal',
            field=models.CharField(max_length=150, unique=True, null=True, blank=True),
        ),
    ]
