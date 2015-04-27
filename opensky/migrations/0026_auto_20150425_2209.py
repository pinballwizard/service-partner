# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0025_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='phone_str',
        ),
        migrations.AddField(
            model_name='office',
            name='phone1',
            field=models.CharField(verbose_name='Телефон офиса', max_length=15, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='office',
            name='phone2',
            field=models.CharField(verbose_name='Телефон техподдержки', max_length=15, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(verbose_name='Контактный адресс', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worker',
            name='email',
            field=models.EmailField(verbose_name='Почта', max_length=75),
            preserve_default=True,
        ),
    ]
