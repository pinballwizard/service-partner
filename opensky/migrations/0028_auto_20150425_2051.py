# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0027_office_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='phone',
            new_name='phone_str',
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Подпись', blank=True),
            preserve_default=True,
        ),
    ]
