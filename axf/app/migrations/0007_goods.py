# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-27 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_foodtypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.IntegerField()),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('marketprice', models.FloatField()),
                ('categoryid', models.CharField(max_length=10)),
                ('childcid', models.CharField(max_length=20)),
                ('childcidname', models.CharField(max_length=200)),
                ('dealerid', models.CharField(max_length=20)),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]
