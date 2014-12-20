# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='current',
        ),
        migrations.RemoveField(
            model_name='city',
            name='users',
        ),
        migrations.RemoveField(
            model_name='city',
            name='visited',
        ),
        migrations.AddField(
            model_name='balance',
            name='current_city',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='balance',
            name='visited_cities',
            field=models.CommaSeparatedIntegerField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
