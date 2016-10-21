# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20161021_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobre_mim',
            name='autho',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='blog_sobre_mim'),
        ),
    ]
