# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-name'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курси'},
        ),
    ]
