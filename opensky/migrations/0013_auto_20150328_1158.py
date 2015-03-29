# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0012_auto_20150327_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(verbose_name='Название', max_length=20)),
                ('logo', models.ImageField(verbose_name='Логотип', upload_to='')),
                ('url', models.URLField(verbose_name='Ссылка')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(verbose_name='Название', unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
