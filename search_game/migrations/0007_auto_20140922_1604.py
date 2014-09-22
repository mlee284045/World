# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_game', '0006_auto_20140922_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
