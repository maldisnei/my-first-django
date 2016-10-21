# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161013_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
    ]
