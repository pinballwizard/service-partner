# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('mark', models.CharField(unique=True, verbose_name='Название', max_length=20)),
                ('text', models.CharField(verbose_name='Текст', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, verbose_name='Наименование', max_length=30)),
                ('description', models.CharField(verbose_name='Описание', max_length=200)),
                ('manufacturer', models.CharField(verbose_name='Производитель', max_length=30)),
                ('price', models.IntegerField(verbose_name='Цена', max_length=10)),
                ('image', models.ImageField(verbose_name='Изображение', upload_to='')),
                ('count', models.IntegerField(verbose_name='Количество', max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('birth_day', models.DateField(verbose_name='День рождения')),
                ('email', models.EmailField(verbose_name='Почта', max_length=75)),
                ('photo', models.ImageField(verbose_name='Фотография', upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
