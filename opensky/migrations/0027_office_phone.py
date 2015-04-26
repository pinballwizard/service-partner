# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0026_auto_20150425_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='phone',
            field=models.CharField(default=1, max_length=100, verbose_name='Телефон офиса'),
            preserve_default=False,
        ),
    ]
