# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0035_auto_20150427_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ImageField(upload_to='', default=1, verbose_name='Изображение для вкладок'),
            preserve_default=False,
        ),
    ]
