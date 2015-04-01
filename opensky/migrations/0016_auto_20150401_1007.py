# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0015_auto_20150401_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialwidget',
            name='url',
            field=models.URLField(verbose_name='Ссылка', blank=True),
            preserve_default=True,
        ),
    ]
