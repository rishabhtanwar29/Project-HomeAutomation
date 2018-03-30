# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-03 07:04
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_auto_20180102_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='label',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='user_name', unique=True),
        ),
    ]