# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60, unique=True)),
                ('password', models.CharField(max_length=60)),
                ('portrait', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('rank', models.CharField(max_length=20)),
                ('sex', models.BooleanField(default=True)),
                ('isdeleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
