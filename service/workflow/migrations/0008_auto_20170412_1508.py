# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20170412_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='response',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caller', to='workflow.Location'),
        ),
    ]
