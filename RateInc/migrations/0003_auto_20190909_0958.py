# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-09 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateInc', '0002_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
