# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(max_digits=7, decimal_places=4)),
                ('longitude', models.DecimalField(max_digits=7, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current', models.BooleanField(default=True)),
                ('city', models.ForeignKey(to='search_game.City')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='search_game.Location'),
            preserve_default=True,
        ),
    ]
