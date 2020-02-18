# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# from .forms import PessoaForm
from django.urls import reverse_lazy

from .forms import PessoaForm
from .models import Pessoa
from crispy_forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

from .util import firstChar

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
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    contexto = {'lista_pessoa':pessoas, 'form':form}
    return render(request, "pessoa/cadastro.html", contexto)

def pessoa_usuario_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('pessoa_usuario')

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