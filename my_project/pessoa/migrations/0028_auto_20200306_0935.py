# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-06 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0027_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, default='pessoa_fotos/none.jpg', help_text='Escolha uma foto para o seu perfil', null=True, upload_to='pessoa_fotos/', verbose_name='Foto'),
        ),
    ]