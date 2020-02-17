# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models

# VALIDADORES
def validate_even(value):
    if value <= 10:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )


# Create your models here.
class Sexo(models.Model):
    """
    Classe para conter os generos adotados no instituto
    model:'pessoa.Pessoa'
    autor:'Ewerton Hallan'
    """
    descricao=models.CharField(
        max_length=20
    )
    def __str__(self):
        return self.descricao


class Pessoa(models.Model):
    nome=models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text='Escreva aqui o seu nome completo',
        verbose_name='Nome Completo',
        error_messages={
            'null':'Valor nulo nao permitido',
            'blank': 'Valor vazio',
        }
    )
    #1-m -> ForeingKey, 1-1 -> OneToOneField, m-m -> ManyToManyField
    genero=models.ForeignKey(Sexo)
    rg=models.IntegerField(
        help_text='Escreva aqui somente os numeros do RG',
        verbose_name='Número do RG',
        unique=True,
    )
    cpf=models.CharField(
        max_length=15,
        help_text='Escreva aqui somente os numeros do CPF',
        verbose_name='Número do CPF',
        unique=True,
        db_index=True,
    )
    estadocivil=models.CharField(
        max_length=20,
        choices=[
            ('S','Solteiro'),
            ('C','Casado'),
            ('V','Viúvo'),
            ('D','Desquitado'),
            ('U','União Estável'),
        ],
        error_messages={
            'invalid_choice':'Valor nao permitido',
        },
        default='S',
        db_index=True,
        verbose_name='Estado Cívil',
    )
    pai=models.CharField(
        max_length=100,
        help_text='Escreva aqui nome completo do seu pai',
        verbose_name='Nome do Pai',
    )
    mae=models.CharField(
        max_length=100,
        help_text='Escreva aqui nome completo do sua mae',
        verbose_name='Nome da Mãe',
    )
    email=models.CharField(
        max_length=200,
        help_text='Escreva aqui o seu e-mail',
        verbose_name='E-Mail',
    )
    telefone=models.CharField(
        max_length=15,
        help_text='Escreva aqui o numero de seu telefone (xx) 99999-9999',
        verbose_name='Telefone',
    )
    idade=models.IntegerField(
        default=0,
        help_text='Coloque aqui sua idade',
        validators=[validate_even],
        verbose_name='Idade',
    )
    foto=models.ImageField(
        upload_to='pessoa_fotos/',
        blank=True,
        help_text = 'Escolha uma foto para o seu perfil',
        verbose_name = 'Foto',
    )
    dt_log=models.DateField(
        auto_now=True,
        editable=False,
        verbose_name='Dt Criação',
    )

    def getPronomeTratamento (self):
        sx = str(self.genero)[0].upper()
        if sx == 'M':
            ptr = 'Sr'
        elif sx == 'F':
            ptr = 'Sra'
        else:
            ptr = ''

        return ptr

    def __str__(self):
        return self.nome

    def __eq__(self, other):
        return self.cpf == other.cpf

    def __ne__(self, other):
        return not (self.__eq__(other))

    # class metadados https://docs.djangoproject.com/en/2.1/ref/models/options/
    class Meta:
        ordering = ['nome', 'idade']
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question + ' - ' + format(self.pub_date, '%d/%m/%Y %H:%M:%S')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice + ' [ ' + self.poll.question + ' ]'

