import re

from django import forms
from .models import *

class Email:
    @staticmethod
    def limpaCampo(txt):
        email = txt
        email = email.replace("[","")
        email = email.replace("u'","")
        email = email.replace("'","")
        email = email.replace("]","")
        email = email.replace(" ","")
        email = email.replace(",",", ")
        return(email)

    @staticmethod
    def is_valid_email(email):
        valid = re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,6}$', email.strip())
        return(valid)


class ValidaEmailField(forms.Field):
    def clean(self, value):
        if not value:
            raise forms.ValidationError('Especifique um e-mail valido !')

        emails = Email.limpaCampo(value)
        emails = emails.split(',')

        for email in emails:
            if not Email.is_valid_email(email):
                raise forms.ValidationError('%s este e-mail nao e um endereco valido !' % email)

        return emails

class PessoaForm(forms.ModelForm):
    #foto = forms.ImageField()
    email = ValidaEmailField()
    email.help_text = 'Escreva aqui o seu e-mail, lista de e-mails separado por "," '
    email.label = 'E-Mail'

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