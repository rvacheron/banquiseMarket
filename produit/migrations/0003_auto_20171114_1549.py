# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_auto_20171108_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]