# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_game', '0002_auto_20140921_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=2),
        ),
    ]
