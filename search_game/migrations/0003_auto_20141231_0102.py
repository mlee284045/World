# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_game', '0002_auto_20141220_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='hidden',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='balance',
            name='current_city',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='balance',
            name='visited_cities',
            field=models.CommaSeparatedIntegerField(max_length=200, null=True, blank=True),
        ),
    ]
