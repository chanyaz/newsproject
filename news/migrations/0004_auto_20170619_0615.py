# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170619_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='reporter',
            field=models.CharField(default='Subin Shrestha', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='reporter_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='reporter_ne',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
