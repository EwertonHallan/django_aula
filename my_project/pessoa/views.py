# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# from .forms import PessoaForm
from django.urls import reverse_lazy

from .forms import PessoaForm, GeneroForm
from .models import Pessoa, Genero
from crispy_forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

from .util import firstChar

class Obj_Lista():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return self.nome

class Obj_Detalhe():
    def __init__(self, titulo, valor):
        self.titulo = titulo
        self.valor = valor
    def __str__(self):
        return self.titulo + '-' + self.valor


# Create your views here.
def pessoa_id(request, p_id):
    pessoas = Pessoa.objects.select_related().get(id=p_id)
    contexto = {'detalhe':pessoas}
    contexto['pronome'] = pessoas.getPronomeTratamento()

    return render(request, 'pessoa/pessoa_id.html', contexto)

def pessoa_list(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        pessoas = Pessoa.objects.all()
        contexto = {'lista_pessoa':pessoas}       #dicionario   [] lista  () tupla
        return render(request, 'pessoa/pessoa_list.html', contexto)

#usa o templete generico de cadastro
def pessoa_usuario(request):
    form = PessoaForm()
    contexto = {'form':form}
    return render(request, "pessoa/cadastro.html", contexto)

def pessoa_usuario_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('pessoa_usuario')

def pessoa_usuario_lista(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Pessoa.objects.all()

        filtro = request.GET
        filtro = request.GET.get('\u201dsearch\u201d')

        if filtro:
            dados = Pessoa.objects.filter(nome__icontains=filtro)

        result = []
        for i in range(len(dados)):
            obj = Obj_Lista(dados[i].id, dados[i].nome)
            result.append(obj)

        #filtro = request.GET.get('\u201dsearch\u201d') + '->' + request.META['REMOTE_ADDR'] + '' + request.user.username
        #filtro = '\u201dsearch\u201d'[1:7]
        contexto = {
            'lista':result,
            'titulo':'Pessoas',
            'url':'/pessoa/usuario_detalhe/',
            'str_busca':filtro
        }
        return render(request, 'pessoa/listagem.html', contexto)

def pessoa_usuario_detalhe(request, p_id):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Pessoa.objects.select_related().get(id=p_id)
        result = []
        result.append(Obj_Detalhe('ID',dados.id))
        result.append(Obj_Detalhe('Nome',dados.getPronomeTratamento() + ' ' + dados.nome))
        result.append(Obj_Detalhe('Pai',dados.pai))
        result.append(Obj_Detalhe('Mae',dados.mae))
        result.append(Obj_Detalhe('RG',dados.rg))
        result.append(Obj_Detalhe('CPF',dados.cpf))
        #result.append(Obj_Detalhe('Foto',"<a href='/upload/" + str(dados.foto) + "' target='_blank'> Visualizar Foto </a>"))
        result.append(Obj_Detalhe('Foto',"<img src='/upload/" + str(dados.foto) + "' width='130px'/>"))

    contexto = {'detalhe':result, 'titulo':'Usuario'}

    return render(request, 'pessoa/detalhe.html', contexto)

def pessoa_genero(request):
    form = GeneroForm()
    contexto = {'form':form}
    return render(request, "pessoa/cadastro.html", contexto)

def pessoa_genero_novo(request):
    form = GeneroForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('pessoa_genero')

def pessoa_genero_lista(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Genero.objects.all()
        result = []
        for i in range(len(dados)):
            obj = Obj_Lista(dados[i].id, dados[i].descricao)
            result.append(obj)

        #contexto = {'lista':result, 'titulo':'Generos', 'url':'/pessoa/genero_detalhe/'}
        contexto = {'lista':result, 'titulo':'Generos', 'url':'/pessoa/genero_detalhe/'}
        return render(request, 'pessoa/listagem.html', contexto)

def pessoa_genero_detalhe(request, p_id):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Genero.objects.select_related().get(id=p_id)
        result = []
        result.append(Obj_Detalhe('ID',dados.id))
        result.append(Obj_Detalhe('Descricao',dados.descricao))

    contexto = {'detalhe':result, 'titulo':'Genero'}

    return render(request, 'pessoa/detalhe.html', contexto)

def pessoa_detalhe(request):
    return render(request, 'pessoa/pessoa_detail.html', {})

def pessoa_sobre(request):
    texto = {'txt':'Texto explicativo sobre o projeto ...'}
    #return HttpResponse('Texto explicativo sobre o projeto')
    return render(request,'pessoa/sobre.html', texto)

def cadastrar_usuario(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    contexto = {'lista_pessoa':pessoas, 'form':form}
    return render(request, "pessoa/cadastro.html", contexto)

#material sobre login https://django-portuguese.readthedocs.io/en/1.0/topics/auth.html
def valida_Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            valida_Login(request, user)
            #redireciona para a pagina inicial
            return render(request, "pessoa/pessoa_list.html", {})
        else:
            #mensagem de erro, retorna a pagina de login
            return render(request, "pessoa/login.html", {})
    else:
        return render(request, "pessoa/login.html", {})

def logoff_User(request):
    logoff_User(request)
    #redireciona para a pagina de login
    return render(request, "pessoa/login.html", {})

#views genericas
#https://django-portuguese.readthedocs.io/en/1.0/intro/tutorial04.html
#documentacao:https://django-portuguese.readthedocs.io/en/1.0/ref/generic-views.html#ref-generic-views