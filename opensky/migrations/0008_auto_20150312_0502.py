# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0007_auto_20150312_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='image',
        ),
        migrations.AddField(
            model_name='feature',
            name='icon',
            field=models.CharField(verbose_name='Название иконки', max_length=20, default='glyphicon-remove'),
            preserve_default=True,
        ),
    ]
