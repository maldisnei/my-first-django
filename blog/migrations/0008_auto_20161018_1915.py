# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('testo', models.TextField()),
                ('auth', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, unique=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True, max_length=100),
        ),
        migrations.AddField(
            model_name='comment',
            name='poste',
            field=models.ForeignKey(related_name='poste', to='blog.Post'),
        ),
    ]
