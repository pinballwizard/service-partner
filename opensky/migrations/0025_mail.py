# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0024_auto_20150406_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sender', models.CharField(max_length=30, verbose_name='Отправитель')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('subject', models.CharField(max_length=50, verbose_name='Тема')),
                ('message', models.TextField(max_length=500, verbose_name='Сообщение')),
            ],
        ),
    ]
