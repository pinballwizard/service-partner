# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0019_auto_20150402_0859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='phone1',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='office',
            name='phone2',
        ),
    ]
