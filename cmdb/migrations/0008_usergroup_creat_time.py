# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0007_auto_20171122_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='creat_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]