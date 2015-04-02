# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensky', '0016_auto_20150401_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.ForeignKey(to='opensky.Worker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='worker',
            name='phone',
        ),
        migrations.AlterField(
            model_name='socialwidget',
            name='name',
            field=models.CharField(max_length=2, choices=[('vk', 'Вконтакте'), ('ok', 'Одноклассники'), ('fb', 'Facebook'), ('tw', 'Twitter'), ('li', 'LinkedIn'), ('yt', 'YouTube'), ('in', 'Instagram')], verbose_name='Название'),
            preserve_default=True,
        ),
    ]
