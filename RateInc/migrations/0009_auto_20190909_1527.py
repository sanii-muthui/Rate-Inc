# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-09 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RateInc', '0008_auto_20190909_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='fbfba5feddcfae6c24fa528c7749eafc.jpg', upload_to='profile/'),
        ),
    ]