# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20171019_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsonspecialplace',
            name='place',
            field=models.IntegerField(choices=[(1, 'NEWS TOP'), (2, 'INDEX TOP'), (3, 'INDEX'), (4, 'ABOUT US')]),
        ),
    ]