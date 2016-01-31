# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160130_1235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About_us',
            new_name='Aboutus',
        ),
    ]
