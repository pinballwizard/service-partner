# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0037_auto_20150505_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(max_length=10000, verbose_name='Описание'),
        ),
    ]
