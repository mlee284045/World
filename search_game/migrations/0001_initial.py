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
            name='Balance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('money', models.DecimalField(default=5000.0, max_digits=7, decimal_places=2)),
                ('found', models.BooleanField(default=False)),
                ('user', models.OneToOneField(related_name=b'balance', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current', models.BooleanField(default=False)),
                ('visited', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=2)),
                ('latitude', models.DecimalField(max_digits=7, decimal_places=4)),
                ('longitude', models.DecimalField(max_digits=7, decimal_places=4)),
                ('users', models.ManyToManyField(related_name=b'cities', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
