# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_auto_20171122_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='title',
            field=models.CharField(db_column='caption', db_index=True, max_length=32),
        ),
    ]