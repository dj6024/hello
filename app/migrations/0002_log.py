# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-08 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('alt', models.CharField(max_length=256)),
            ],
        ),
    ]