# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 12:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Ім’я')),
                ('last_name', models.CharField(max_length=30, verbose_name='Призвіще')),
                ('email', models.EmailField(max_length=254, verbose_name='електронна пошта')),
                ('phone', models.CharField(max_length=25, verbose_name='телефон')),
                ('date_of_birth', models.DateField(verbose_name='дата народження')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='користувач')),
            ],
            options={
                'verbose_name_plural': 'Вчителі',
                'verbose_name': 'Вчитель',
            },
        ),
    ]
