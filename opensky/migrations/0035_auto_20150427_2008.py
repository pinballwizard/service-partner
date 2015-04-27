# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0034_auto_20150426_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='image',
        ),
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]
