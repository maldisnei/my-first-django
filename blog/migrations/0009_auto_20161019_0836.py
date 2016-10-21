# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161018_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auth',
            new_name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_appoved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='poste',
            field=models.ForeignKey(related_name='comments', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(max_length=100, blank=True, unique=True),
        ),
    ]
