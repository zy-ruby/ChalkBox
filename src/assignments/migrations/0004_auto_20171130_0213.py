# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_auto_20171122_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='assigment_description',
            new_name='description',
        ),
    ]
