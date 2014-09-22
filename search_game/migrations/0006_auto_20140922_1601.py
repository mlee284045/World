# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_game', '0005_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='found',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='balance',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='balance',
            name='money',
            field=models.DecimalField(default=5000.0, max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='balance',
            name='start',
            field=models.DateTimeField(blank=True),
        ),
    ]
