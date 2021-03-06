# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=200)),
                ('categoryid', models.CharField(max_length=10)),
                ('brandname', models.CharField(max_length=1000)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=10)),
                ('productid1', models.CharField(max_length=20)),
                ('longname1', models.CharField(max_length=200)),
                ('price1', models.FloatField()),
                ('marketprice1', models.FloatField()),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=10)),
                ('productid2', models.CharField(max_length=20)),
                ('longname2', models.CharField(max_length=200)),
                ('price2', models.FloatField()),
                ('marketprice2', models.FloatField()),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=10)),
                ('productid3', models.CharField(max_length=20)),
                ('longname3', models.CharField(max_length=200)),
                ('price3', models.FloatField()),
                ('marketprice3', models.FloatField()),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]
