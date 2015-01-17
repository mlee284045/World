# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_game', '0004_auto_20150116_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='restarts',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='balance',
            name='wins',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
