# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 20:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Licencias',
            new_name='Licencia',
        ),
    ]