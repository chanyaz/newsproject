# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OfficeStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='staff_photos/')),
                ('special', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='StaffMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.OfficeStaff')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
