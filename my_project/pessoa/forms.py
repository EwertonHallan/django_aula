from django import forms
from .models import *

class PessoaForm(forms.ModelForm):
    #foto = forms.ImageField()

    class Meta:
        model = Pessoa
        fields = ["nome", "genero", "estadocivil", "idade", "pai", "mae",
                  "rg", "cpf", "email", "telefone", "foto"
                  ]

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ["descricao"]


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ["descricao", "file"]