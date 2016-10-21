# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20161019_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_appoved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True, max_length=200),
        ),
    ]
