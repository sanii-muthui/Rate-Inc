# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-09 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RateInc', '0006_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='like',
            name='liked_by',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
