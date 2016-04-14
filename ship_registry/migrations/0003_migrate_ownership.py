# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 08:22
from __future__ import unicode_literals

from datetime import datetime

from django.db import migrations
from django.utils import timezone


DEFAULT_BEGIN = timezone.make_aware(datetime.fromtimestamp(0))

def migrate_ownership(apps, schema_editor):
    Ship = apps.get_model('ship_registry', 'Ship')
    ShipOwnership = apps.get_model('ship_registry', 'ShipOwnership')
    for ship in Ship.objects.all():
        if ship.owner is not None:
            ShipOwnership.objects.create(company=ship.owner, ship=ship, begin=DEFAULT_BEGIN)


class Migration(migrations.Migration):

    dependencies = [
        ('ship_registry', '0002_add_ownership'),
    ]

    operations = [
        migrations.RunPython(migrate_ownership),
    ]
