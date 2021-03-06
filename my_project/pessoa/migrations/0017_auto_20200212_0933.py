# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-12 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0016_my_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'ordering': ['nome', 'idade'], 'verbose_name': 'pessoa', 'verbose_name_plural': 'pessoas'},
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='estadocivil',
            field=models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('V', 'Viuvo'), ('D', 'Desquitado'), ('U', 'Uniao Estavel')], db_index=True, default='S', error_messages={'invalid_choice': 'Valor nao permitido'}, max_length=20),
        ),
    ]
