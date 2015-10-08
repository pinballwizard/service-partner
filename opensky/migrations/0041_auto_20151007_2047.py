# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0040_auto_20150507_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(verbose_name='Описание', max_length=5000),
        ),
    ]
