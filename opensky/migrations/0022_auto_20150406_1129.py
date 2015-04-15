# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0021_auto_20150402_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.CharField(verbose_name='Текст', max_length=20000),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_str',
            field=models.CharField(verbose_name='Контактный телефон (через ;)', max_length=100),
        ),
        migrations.AlterField(
            model_name='worker',
            name='email',
            field=models.EmailField(verbose_name='Почта', max_length=254),
        ),
    ]
