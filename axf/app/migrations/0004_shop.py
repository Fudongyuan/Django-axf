# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]
