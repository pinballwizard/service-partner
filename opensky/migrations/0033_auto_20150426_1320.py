# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0032_auto_20150426_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='maptype',
            field=models.CharField(default='yandex#map', choices=[('yandex#map', 'Схема'), ('yandex#satellite', 'Спутник'), ('yandex#hybrid', 'Гибрид'), ('yandex#publicMap', 'Народная'), ('yandex#publicMapHybrid', 'Народная+Гибрид')], verbose_name='Тип карты', max_length=30),
        ),
        migrations.AlterField(
            model_name='worker',
            name='email',
            field=models.EmailField(verbose_name='Почта', max_length=254),
        ),
    ]
