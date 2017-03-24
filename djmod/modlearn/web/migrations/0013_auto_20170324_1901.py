# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20170321_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='new post', error_messages={'blank': 'this is blank field', 'required': 'the field is required', 'unique': 'this title is not unique'}, help_text='must be a unique title', max_length=240, unique=True, verbose_name='post title'),
        ),
    ]
