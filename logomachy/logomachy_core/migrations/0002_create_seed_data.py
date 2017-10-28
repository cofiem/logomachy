# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 23:37
from __future__ import unicode_literals

import os
from django.db import migrations

from logomachy.logomachy_auth.models import User


def create_seed_data(apps, schema_editor):
    # We can't import the models directly as there may be a newer
    # version than this migration expects. We use the historical version.

    # create the superuser using the real User model, as it does not work using
    # the apps.get_model object (AttributeError: type object 'User' has no attribute 'normalize_username')
    admin = User.objects.create_superuser(
        username=os.getenv('DJANGO_ADMIN_USER_NAME', 'admin'),
        email=os.getenv('DJANGO_ADMIN_USER_EMAIL', 'example@example.com'),
        password=os.getenv('DJANGO_ADMIN_USER_PASS', 'ADefaultPassword')
    )
    admin.is_active = True
    admin.save()

    DocumentType = apps.get_model('logomachy_core', 'DocumentType')  # type: DocumentType
    eula = DocumentType(
        name='eula',
        description="An end-user license agreement (EULA) or software license agreement is the contract between the "
                    "licensor and purchaser, establishing the purchaser's right to use the proprietary software. "
                    "(descr from Wikipedia)")
    eula.full_clean()
    eula.save()

    tos = DocumentType(
        name='tos',
        description="Terms of service (terms of use, terms and conditions, ToS) are rules by  which one must agree "
                    "to abide in order to use a service. Terms of service can also be merely a disclaimer, "
                    "especially regarding the use of websites. (descr from Wikipedia)")
    tos.full_clean()
    tos.save()

    pp = DocumentType(
        name='privacy_policy',
        description="A privacy policy is a statement or a legal document that discloses some or all of the ways a "
                    "party gathers, uses, discloses, and manages a customer or client's data. (descr from Wikipedia)")
    pp.full_clean()
    pp.save()


def remove_seed_data(apps, schema_editor):
    User.objects.get(name=os.getenv('DJANGO_ADMIN_USER_NAME', 'admin')).delete()

    DocumentType = apps.get_model('logomachy_core', 'DocumentType')  # type: DocumentType
    DocumentType.objects.get(name='eula').delete()
    DocumentType.objects.get(name='tos').delete()
    DocumentType.objects.get(name='privacy policy').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('logomachy_core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_seed_data, remove_seed_data)
    ]
