# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160314_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cereal',
            old_name='sugar',
            new_name='sugars',
        ),
    ]
