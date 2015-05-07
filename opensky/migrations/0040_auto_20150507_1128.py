# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0039_auto_20150507_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoringPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
            ],
        ),
        migrations.RenameModel(
            old_name='Price',
            new_name='EquipmentPrice',
        ),
    ]
