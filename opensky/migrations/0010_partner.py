# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0009_auto_20150313_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
