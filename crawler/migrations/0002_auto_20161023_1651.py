# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemurl',
            name='item_content',
            field=models.CharField(max_length=2000),
        ),
    ]