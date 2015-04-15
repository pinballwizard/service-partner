# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0023_auto_20150406_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=20000, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(max_length=200, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='text',
            field=models.TextField(max_length=10000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Описание'),
        ),
    ]
