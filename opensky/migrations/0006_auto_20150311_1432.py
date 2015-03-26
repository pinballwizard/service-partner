# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0005_auto_20150311_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', models.ImageField(verbose_name='Картинка', upload_to='')),
                ('text', models.CharField(verbose_name='Подпись', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='image',
            field=models.ImageField(verbose_name='Картинка', upload_to='carousel'),
            preserve_default=True,
        ),
    ]
