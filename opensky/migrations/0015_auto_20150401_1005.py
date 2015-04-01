# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0014_auto_20150329_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialwidget',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='socialwidget',
            name='mark',
        ),
        migrations.AddField(
            model_name='socialwidget',
            name='name',
            field=models.CharField(verbose_name='Название', choices=[('vk', 'Вконтакте'), ('ok', 'Одноклассники'), ('fb', 'Facebook'), ('tw', 'Twitter')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='price',
            name='name',
            field=models.CharField(verbose_name='Название', max_length=30),
            preserve_default=True,
        ),
    ]
