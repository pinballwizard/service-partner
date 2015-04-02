# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0018_auto_20150402_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.RenameField(
            model_name='office',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AddField(
            model_name='office',
            name='phone2',
            field=models.CharField(max_length=100, verbose_name='Запасной телефон', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Телефон', default=1),
            preserve_default=False,
        ),
    ]
