# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-22 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0003_auto_20181022_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='creativity',
            field=models.CharField(max_length=8, null=True),
        ),
    ]