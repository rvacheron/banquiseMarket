# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
        ('panier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='panier',
            name='produtis',
            field=models.ManyToManyField(to='produit.Produit'),
        ),
    ]
