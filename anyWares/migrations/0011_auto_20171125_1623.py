# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-25 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anyWares', '0010_auto_20171125_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.FileField(null=True, upload_to='static/'),
        ),
    ]
