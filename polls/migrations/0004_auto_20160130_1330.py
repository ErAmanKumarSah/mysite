# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160130_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 30, 8, 0, 50, 879128, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='texting',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
