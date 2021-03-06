# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20181128_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
    ]
