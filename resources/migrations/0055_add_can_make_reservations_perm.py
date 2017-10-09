# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0054_add_reservation_participants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ('name',), 'permissions': (('can_approve_reservation', 'Can approve reservation'), ('can_make_reservations', 'Can make reservations'), ('can_view_reservation_access_code', 'Can view reservation access code'), ('can_view_reservation_extra_fields', 'Can view reservation extra fields'), ('can_access_reservation_comments', 'Can access reservation comments'), ('can_view_reservation_catering_orders', 'Can view reservation catering orders')), 'verbose_name': 'unit', 'verbose_name_plural': 'units'},
        ),
    ]
