# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0017_auto_20150402_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='owner',
            field=models.ForeignKey(to='opensky.Worker', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=10),
            preserve_default=True,
        ),
    ]
