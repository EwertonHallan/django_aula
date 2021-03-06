# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-07 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_myproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.IntegerField(help_text='Escreva aqui somente os numeros do CPF', verbose_name='Numero do CPF:'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='estadocivil',
            field=models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(help_text='Escreva aqui o seu nome completo', max_length=100, verbose_name='Nome Completo:'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='rg',
            field=models.IntegerField(help_text='Escreva aqui somente os numeros do RG', verbose_name='Numero do RG:'),
        ),
    ]
