# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0003_carouselimage_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='position',
            field=models.IntegerField(max_length=1, verbose_name='Позиция'),
            preserve_default=True,
        ),
    ]
