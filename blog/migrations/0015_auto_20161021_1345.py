# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20161021_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sobre_mim',
            old_name='testo',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='sobre_mim',
            old_name='titulo',
            new_name='title',
        ),
    ]
