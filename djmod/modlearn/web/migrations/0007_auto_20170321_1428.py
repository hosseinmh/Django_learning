# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20170321_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
