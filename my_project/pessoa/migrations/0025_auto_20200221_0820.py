# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-21 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0024_auto_20200221_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to='pessoa_fotos/'),
        ),
    ]
