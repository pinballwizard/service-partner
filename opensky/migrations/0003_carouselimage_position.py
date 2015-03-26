# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0002_carouselimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimage',
            name='position',
            field=models.IntegerField(default=1, max_length=1, unique=True, verbose_name='Позиция'),
            preserve_default=False,
        ),
    ]
