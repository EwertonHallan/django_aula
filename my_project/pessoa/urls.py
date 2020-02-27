"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.pessoa_usuario_lista, name='livros_info'),
    #url(r'^lista/$', views.pessoa_list, name='livros_info'),
    url(r'^id/(?P<p_id>[0-9]{,2})/$', views.pessoa_id, name='Detalhe_ID'),
    #url(r'^cadastro/$', views.cadastrar_usuario, name='Cadastro'),
    url(r'^upload/$', views.simple_upload, name='Upload'),
    url(r'^usuario/$', views.pessoa_usuario, name='pessoa_usuario'),
    url(r'^usuario_novo/', views.pessoa_usuario_novo, name='pessoa_usuario_novo'),
    url(r'^usuario_edicao/(?P<p_id>\d+)/$', views.pessoa_usuario_edicao, name='pessoa_usuario_edicao'),
    url(r'^usuario_remove/(?P<p_id>\d+)/$', views.pessoa_usuario_remove, name='pessoa_usuario_remove'),
    url(r'^usuario_listagem/', views.pessoa_usuario_lista, name='pessoa_usuario_lista'),
    url(r'^usuario_detalhe/(?P<p_id>[0-9]{,2})/$', views.pessoa_usuario_detalhe, name='pessoa_usuario_detalhe'),
    url(r'^genero/$', views.pessoa_genero, name='pessoa_genero'),
    url(r'^genero_novo/', views.pessoa_genero_novo, name='pessoa_genero_novo'),
    url(r'^genero_edicao/(?P<p_id>\d+)/$', views.pessoa_genero_edicao, name='pessoa_genero_edicao'),
    url(r'^genero_remove/(?P<p_id>\d+)/$', views.pessoa_genero_remove, name='pessoa_genero_remove'),
    url(r'^genero_listagem/', views.pessoa_genero_lista, name='pessoa_genero_lista'),
    url(r'^genero_detalhe/(?P<p_id>[0-9]{,2})/$', views.pessoa_genero_detalhe, name='pessoa_genero_detalhe'),
    url(r'^permission_error/', views.pessoa_permission_error, name='pessoa_erro_permissao'),
    url(r'^detalhe/$', views.pessoa_detalhe, name='Detalhe'),
    url(r'^sobre/', views.pessoa_sobre, name='Sobre'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
