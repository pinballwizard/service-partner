# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0028_auto_20150425_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='phone_str',
        ),
    ]
