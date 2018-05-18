# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180517_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',)},
        ),
    ]
