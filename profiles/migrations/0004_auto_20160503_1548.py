# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-03 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20160503_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='state_of_residence',
            new_name='state',
        ),
    ]
