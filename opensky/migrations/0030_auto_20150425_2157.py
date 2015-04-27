# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0029_remove_office_phone_str'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='phone1',
        ),
        migrations.RemoveField(
            model_name='office',
            name='phone2',
        ),
        migrations.AddField(
            model_name='office',
            name='phone_str',
            field=models.CharField(max_length=100, verbose_name='Контактный телефон (через ;)', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Подпись'),
            preserve_default=True,
        ),
    ]
