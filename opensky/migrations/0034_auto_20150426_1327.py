# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0033_auto_20150426_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=100, blank=True, verbose_name='Контактный адресс'),
        ),
        migrations.AlterField(
            model_name='office',
            name='email',
            field=models.EmailField(max_length=50, blank=True, verbose_name='Контактная почта'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone1',
            field=models.CharField(max_length=15, blank=True, verbose_name='Телефон офиса'),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone2',
            field=models.CharField(max_length=15, blank=True, verbose_name='Телефон техподдержки'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='Цена'),
        ),
    ]
