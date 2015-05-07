# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0038_auto_20150505_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='count',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='price',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='manufacturer',
            field=models.CharField(max_length=60, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(unique=True, max_length=60, verbose_name='Наименование'),
        ),
    ]
