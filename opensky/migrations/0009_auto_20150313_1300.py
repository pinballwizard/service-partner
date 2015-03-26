# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0008_auto_20150312_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('icon', models.CharField(verbose_name='Название иконки', default='glyphicon-remove', max_length=20)),
                ('text', models.CharField(verbose_name='Текст', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='feature',
            name='header',
            field=models.CharField(verbose_name='Заголовок', default='Вставьте заголовок', max_length=100),
            preserve_default=True,
        ),
    ]
