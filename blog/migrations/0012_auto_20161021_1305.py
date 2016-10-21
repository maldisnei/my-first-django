# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0011_auto_20161019_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre_mim',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=200)),
                ('testo', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sobre_mim')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
