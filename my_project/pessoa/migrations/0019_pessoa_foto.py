# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-13 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0018_auto_20200212_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, help_text='Escolha uma foto para o seu perfil', upload_to=b'', verbose_name='Foto'),
        ),
    ]
