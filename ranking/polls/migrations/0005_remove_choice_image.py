# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 07:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170603_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='image',
        ),
    ]
