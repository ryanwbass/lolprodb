# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-24 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anyWares', '0007_auto_20171124_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='filename',
            new_name='fileReference',
        ),
    ]
