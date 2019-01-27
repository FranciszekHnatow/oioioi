# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-29 22:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'contestexcl', '0004_auto_20190129_1904'), (b'contestexcl', '0005_auto_20190129_2230')]

    dependencies = [
        ('contestexcl', '0003_exclusivenessconfig_enable_helptext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exclusivenessconfig',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contest'),
        ),
        migrations.AlterField(
            model_name='exclusivenessconfig',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
        ),
    ]
