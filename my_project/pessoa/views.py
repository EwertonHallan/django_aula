# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# from .forms import PessoaForm
from django.urls import reverse_lazy

from .forms import *
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

#teste de upload

def simple_upload(request):
    if request.method == 'POST':
        filename = ''

        if request.FILES['file']:
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save('pessoa_fotos/'+myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

        form = DocumentoForm(request.POST or None)
        form.cleaned_data['foto'] = filename
        if form.is_valid():
            form.save()

        return render(request, 'pessoa/upload.html', {
            'uploaded_file_url': uploaded_file_url, 'form':form
        })

    form = DocumentoForm()
    contexto = {'form':form}
    return render(request, 'pessoa/upload.html', contexto)

def pessoa_permission_error(request):
    link = {'link':request.GET.get('next')}
    return render(request, 'pessoa/erro_permissao.html', link)

# Create your views here.
@login_required(login_url='/login/')
@permission_required('pessoa.change_pessoa',login_url='/pessoa/permission_error/')
#@permission_required('pessoa.add_pessoa',raise_exception=True)
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
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        if not(request.user.has_perm('pessoa.add_pessoa')):
            return redirect('/pessoa/permission_error/?next=/pessoa/usuario/')

        form = PessoaForm()
        url_form = url_form = '/pessoa/usuario_novo/'
        contexto = {
            'form':form,
            'titulo':'Ficha de Cadastro [NOVO]',
            'url_form':url_form
        }
        return render(request, "pessoa/cadastro.html", contexto)

def pessoa_usuario_novo(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        if not(request.user.has_perm('pessoa.add_pessoa')):
            return redirect('/pessoa/permission_error/?next=/pessoa/usuario_novo/')

        form = PessoaForm(request.POST or None)
        filename = ''
        if request.FILES.has_key('foto'):
            myfile = request.FILES['foto']
            fs = FileSystemStorage()
            filename = fs.save('pessoa_fotos/' + myfile.name, myfile)

        if form.is_valid():
            if len(filename) > 0:
                form = form.save(commit=False)
                form.foto = filename

            form.save()
        return redirect('pessoa_usuario')

def pessoa_usuario_edicao(request, p_id):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        if not(request.user.has_perm('pessoa.change_pessoa')):
            return redirect('/pessoa/permission_error/?next=/pessoa/usuario_edicao/')

        dados = Pessoa.objects.select_related().get(id=p_id)
        form = PessoaForm(request.POST or None, instance=dados)
        if request.method == 'POST':
            filename = ''
            if request.FILES.has_key('foto'):
                myfile = request.FILES['foto']
                fs = FileSystemStorage()
                filename = fs.save('pessoa_fotos/' + myfile.name, myfile)

            if form.is_valid():
                if len(filename) > 0:
                    form = form.save(commit=False)
                    form.foto = filename
                form.save()

                return redirect('pessoa_usuario_lista')
        else:
            url_form = url_form = '/pessoa/usuario_edicao/'+str(dados.id)+'/'
            contexto = {
                'dados':dados,
                'form': form,
                'titulo': 'Ficha de Cadastro [MODIFICACAO]',
                'url_form': url_form
                }
            return render(request,'pessoa/cadastro.html',contexto)

def pessoa_usuario_remove(request, p_id):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        if not(request.user.has_perm('pessoa.delete_pessoa')):
            return redirect('/pessoa/permission_error/?next=/pessoa/usuario_remove/')

        dados = Pessoa.objects.select_related().get(id=p_id)
        if request.method == 'POST':
            dados.delete()
            return redirect('pessoa_usuario_lista')
        else:
            url_form = '/pessoa/usuario_remove/'+str(dados.id)+'/'
            url_detalhe = '/pessoa/usuario_detalhe/'+str(dados.id)+'/'
            contexto = {
                'url_form':url_form,
                'url_detalhe':url_detalhe,
                'dados': dados,
            }
            return render(request,'pessoa/confirmacao.html', contexto)

@login_required(login_url='/login/')
#@permission_required('pessoa.add_pessoa',login_url='/pessoa/permission_error/')
#criacao de permissao https://docs.djangoproject.com/pt-br/1.11/topics/auth/default/
def pessoa_usuario_lista(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        if not(request.user.has_perm('pessoa.list_pessoa')):
            return redirect('/pessoa/permission_error/?next=/pessoa/usuario_listagem/')

        dados = Pessoa.objects.all().order_by('-nome','id')

        filtro = request.GET
        filtro = request.GET.get('\u201dsearch\u201d')

        if filtro:
            dados = Pessoa.objects.filter(nome__icontains=filtro).order_by('?')

        result = []
        for i in range(len(dados)):
            obj = Obj_Lista(dados[i].id, dados[i])
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
        #url_img = '/upload/' + str(dados.foto)

        url_img = ''
        if dados.foto:
            url_img = dados.foto.url
        result.append(Obj_Detalhe('Foto',"<img src='" + url_img + "' class='img-fluid' />"))

    #contexto = {'detalhe':result, 'titulo':'Usuario','parametro_id':p_id}

    contexto = {
        'detalhe':result,
        'titulo':'Usuario',
        'url_edicao':'/pessoa/usuario_edicao/'+str(p_id)+'/',
        'url_remocao':'/pessoa/usuario_remove/'+str(p_id)+'/',
    }

    return render(request, 'pessoa/detalhe.html', contexto)

def pessoa_genero(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        form = GeneroForm()
        url_form = url_form = '/pessoa/genero_novo/'
        contexto = {
            'form':form,
            'titulo':'Cadastro de Genero [NOVO]',
            'url_form':url_form
        }
        return render(request, "pessoa/cadastro.html", contexto)

def pessoa_genero_novo(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        form = GeneroForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('pessoa_genero')

def pessoa_genero_edicao(request, p_id):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Genero.objects.select_related().get(id=p_id)
        form = GeneroForm(request.POST or None, instance=dados)
        if request.method == 'POST':
            if form.is_valid():
                form.save()

                return redirect('pessoa_genero_lista')
        else:
            url_form = url_form = '/pessoa/genero_edicao/' + str(dados.id) + '/'
            contexto = {
                'dados':dados,
                'form': form,
                'titulo': 'Cadastro de Genero [MODIFICACAO]',
                'url_form':url_form
                }
            return render(request,'pessoa/cadastro.html',contexto)

def pessoa_genero_remove(request, p_id):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Genero.objects.select_related().get(id=p_id)
        if request.method == 'POST':
            dados.delete()
            return redirect('pessoa_genero_lista')
        else:
            url_form = '/pessoa/genero_remove/'+str(dados.id)+'/'
            url_detalhe = '/pessoa/genero_detalhe/'+str(dados.id)+'/'
            contexto = {
                'url_form':url_form,
                'url_detalhe':url_detalhe,
                'dados': dados,
            }
            return render(request,'pessoa/confirmacao.html', contexto)

def pessoa_genero_lista(request):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Genero.objects.all()
        filtro = request.GET
        filtro = request.GET.get('\u201dsearch\u201d')
        if filtro:
            dados = Genero.objects.filter(descricao__icontains=filtro)

        result = []
        for i in range(len(dados)):
            obj = Obj_Lista(dados[i].id, dados[i])
            result.append(obj)

        contexto = {
            'lista':result,
            'titulo':'Generos',
            'url':'/pessoa/genero_detalhe/',
            'str_busca': filtro
        }
        return render(request, 'pessoa/listagem.html', contexto)

def pessoa_genero_detalhe(request, p_id):
    if not(request.user.is_authenticated):
       return redirect('login')
    else:
        dados = Genero.objects.select_related().get(id=p_id)
        result = []
        result.append(Obj_Detalhe('ID',dados.id))
        result.append(Obj_Detalhe('Descricao',dados.descricao))

    contexto = {
        'detalhe':result,
        'titulo':'Genero',
        'url_edicao':'/pessoa/genero_edicao/'+str(p_id)+'/',
        'url_remocao':'/pessoa/genero_remove/'+str(p_id)+'/',
    }

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