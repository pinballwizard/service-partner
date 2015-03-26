# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(verbose_name='Картинка', upload_to='')),
                ('text', models.CharField(verbose_name='Подпись', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
