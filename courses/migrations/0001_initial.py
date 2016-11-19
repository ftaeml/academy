# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='назва')),
                ('description', models.CharField(max_length=100, verbose_name='опис')),
                ('start', models.DateField(verbose_name='початок курсу')),
                ('end', models.DateField(verbose_name='закінчення курсу')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
            options={
                'verbose_name_plural': 'Курси',
                'verbose_name': 'Курс',
            },
        ),
    ]
