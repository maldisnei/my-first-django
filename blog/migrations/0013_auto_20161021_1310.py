# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20161021_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sobre_mim',
            old_name='author',
            new_name='autho',
        ),
    ]
