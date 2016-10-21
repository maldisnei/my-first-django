# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161013_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(upload_to='blog/static/blog', blank=True, null=True),
        ),
    ]
