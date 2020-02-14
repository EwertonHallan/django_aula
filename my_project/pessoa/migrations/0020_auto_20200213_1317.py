# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-13 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0019_pessoa_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, help_text='Escolha uma foto para o seu perfil', upload_to='pessoa_fotos/', verbose_name='Foto'),
        ),
    ]
