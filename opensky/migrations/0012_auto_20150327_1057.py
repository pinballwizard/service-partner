# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0011_auto_20150327_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(verbose_name='Контактный адресс', max_length=50)),
                ('email', models.EmailField(verbose_name='Контактная почта', max_length=50)),
                ('phone', models.CharField(verbose_name='Контактный телефон', max_length=100)),
                ('latitude', models.CharField(verbose_name='Широта', max_length=10)),
                ('longitude', models.CharField(verbose_name='Долгота', max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='worker',
            name='phone',
            field=models.CharField(verbose_name='Телефон', default=1, max_length=10),
            preserve_default=False,
        ),
    ]
