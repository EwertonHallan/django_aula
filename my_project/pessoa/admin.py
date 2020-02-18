# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import  admin

from .models import *

# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields':('nome','genero','estadocivil','idade')}),
        ('Filiacao', {'fields':('pai','mae')}),
        ('Documentos', {'fields':('rg','cpf')}),
        ('Complemento', {'fields': ('email', 'telefone', 'foto')}),
    )
    list_display = ('id','nome','cpf','idade', 'genero','mae','dt_log')
    search_fields = ('nome','cpf','idade', 'mae','genero__descricao')
    list_filter = ('genero', 'estadocivil')



#admin.site.register(Pessoa)
#admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Genero)


