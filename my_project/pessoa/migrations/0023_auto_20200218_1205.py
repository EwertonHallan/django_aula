# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-18 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0022_auto_20200218_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='descricao',
            field=models.CharField(error_messages={'blank': 'Valor vazio', 'null': 'Valor nulo nao permitido'}, help_text='Escreva aqui o nome do genero', max_length=20, verbose_name='Nome do Genero'),
        ),
    ]
