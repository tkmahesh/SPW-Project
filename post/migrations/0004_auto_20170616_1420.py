# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170616_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='postimages'),
        ),
    ]
