# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 15:34
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0016_auto_20170420_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transition',
            name='permanent_tokens',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
    ]
