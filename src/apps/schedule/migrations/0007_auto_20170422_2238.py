# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_dataconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataconfig',
            name='last_update',
            field=models.DateField(auto_now=True),
        ),
    ]
