# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import news.storage


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20171017_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='banner',
            field=models.ImageField(storage=news.storage.NewsImageStorage(), upload_to='static/news/banner'),
        ),
    ]
