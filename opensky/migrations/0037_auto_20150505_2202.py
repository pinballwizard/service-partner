# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0036_feature_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
