# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0031_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='maptype',
            field=models.CharField(default='yandex#map', choices=[('yandex#map', 'Схема'), ('yandex#satellite', 'Спутник'), ('yandex#hybrid', 'Гибрид'), ('yandex#publicMap', 'Народная'), ('yandex#publicMapHybrid', 'Народная+Гибрид')], max_length=30, verbose_name='Тип карты'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='text',
            field=models.CharField(verbose_name='Подпись', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
