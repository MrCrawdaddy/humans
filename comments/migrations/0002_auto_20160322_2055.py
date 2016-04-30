# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='appropriate',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='checked_by_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='documentary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentaries.Documentary'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
