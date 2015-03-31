# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0013_auto_20150328_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название', max_length=20)),
                ('price', models.IntegerField(verbose_name='Цена', max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='feature',
            name='text',
            field=models.CharField(verbose_name='Описание', max_length=10000),
            preserve_default=True,
        ),
    ]
