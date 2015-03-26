# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0006_auto_20150311_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='header',
            field=models.CharField(verbose_name='Заголовок', max_length=30, default='Вставьте заголовок'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feature',
            name='text',
            field=models.CharField(verbose_name='Текст', max_length=100),
            preserve_default=True,
        ),
    ]
