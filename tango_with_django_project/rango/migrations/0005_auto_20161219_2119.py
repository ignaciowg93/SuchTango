# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
