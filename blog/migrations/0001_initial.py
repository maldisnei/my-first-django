# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(null=True, upload_to='static/blog/imagens', blank=True)),
            ],
        ),
    ]
