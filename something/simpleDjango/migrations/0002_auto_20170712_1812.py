# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleDjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='parent_catalog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simpleDjango.Catalog', verbose_name='Родительский каталог'),
        ),
    ]
