# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helusers', '0001_add_ad_groups'),
        ('users', '0006_auto_20161110_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ad_groups',
            field=models.ManyToManyField(blank=True, to='helusers.ADGroup'),
        ),
    ]
