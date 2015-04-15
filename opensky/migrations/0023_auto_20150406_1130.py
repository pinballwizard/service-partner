# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0022_auto_20150406_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='position',
            field=models.IntegerField(unique=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='count',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
