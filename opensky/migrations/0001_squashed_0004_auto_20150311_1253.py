# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [('opensky', '0001_initial'), ('opensky', '0002_carouselimage'), ('opensky', '0003_carouselimage_position'), ('opensky', '0004_auto_20150311_1253')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('mark', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('text', models.CharField(max_length=500, verbose_name='Текст')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('manufacturer', models.CharField(max_length=30, verbose_name='Производитель')),
                ('price', models.IntegerField(max_length=10, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('count', models.IntegerField(max_length=2, verbose_name='Количество')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birth_day', models.DateField(verbose_name='День рождения')),
                ('email', models.EmailField(max_length=75, verbose_name='Почта')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('text', models.CharField(max_length=100, verbose_name='Подпись')),
                ('position', models.IntegerField(max_length=1, verbose_name='Позиция')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
