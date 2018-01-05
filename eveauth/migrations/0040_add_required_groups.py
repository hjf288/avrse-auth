# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-30 16:46
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.models import Group


def add_groups(*args, **kwargs):
    admin, admin_created = Group.objects.get_or_create(name="admin")
    fc, fc_created = Group.objects.get_or_create(name="FC")

    if admin_created:
        admin.details.is_open = True
        admin.details.forum = True
        admin.details.discord = True
        admin.details.save()

    if fc_created:
        fc.details.can_apply = True
        fc.details.forum = True
        fc.details.discord = True
        fc.details.save()


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0039_auto_20171230_1646'),
    ]

    operations = [
        migrations.RunPython(add_groups),
    ]