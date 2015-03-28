# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0010_partner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='header',
            field=models.CharField(max_length=100, verbose_name='Заголовок', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='header',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feature',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Описание'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Описание'),
            preserve_default=True,
        ),
    ]
