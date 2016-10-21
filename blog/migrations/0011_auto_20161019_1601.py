# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161019_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_appoved',
            new_name='approved_comment',
        ),
    ]
