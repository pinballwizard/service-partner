# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0020_auto_20150402_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='phone',
            new_name='phone_str',
        ),
    ]
