# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
    ]
