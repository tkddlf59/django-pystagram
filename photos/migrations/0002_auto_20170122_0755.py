# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
