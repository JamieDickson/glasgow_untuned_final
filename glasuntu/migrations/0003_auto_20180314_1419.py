# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-14 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glasuntu', '0002_auto_20180314_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venuepage',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
