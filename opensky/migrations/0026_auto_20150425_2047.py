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
            field=models.CharField(default=1, max_length=15, verbose_name='Телефон офиса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='office',
            name='phone2',
            field=models.CharField(default=1, max_length=15, verbose_name='Телефон техподдержки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Контактный адресс'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='worker',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='Почта'),
            preserve_default=True,
        ),
    ]
