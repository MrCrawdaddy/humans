# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-17 21:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField()),
                ('comment', models.TextField()),
                ('appropriate', models.BooleanField()),
                ('checked_by_admin', models.BooleanField()),
                ('documentary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='documentaries.Documentary')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
