# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_game', '0003_auto_20141231_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='current_city',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='balance',
            name='hidden',
            field=models.IntegerField(default=1),
        ),
    ]
