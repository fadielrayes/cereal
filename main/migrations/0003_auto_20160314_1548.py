# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160314_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='manufacturer_for_cereal',
            new_name='manufacturer',
        ),
        migrations.RenameField(
            model_name='cereal',
            old_name='name_of_cereal',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cereal',
            old_name='sugars',
            new_name='sugar',
        ),
    ]
