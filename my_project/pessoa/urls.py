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
    url(r'^$', views.pessoa_list, name='livros_info'),
    url(r'^lista/$', views.pessoa_list, name='livros_info'),
    url(r'^id/(?P<p_id>[0-9]{,2})/$', views.pessoa_id, name='Detalhe_ID'),
    url(r'^usuario/$', views.pessoa_usuario, name='pessoa_usuario'),
    url(r'^usuario_novo/', views.pessoa_usuario_novo, name='pessoa_usuario_novo'),
    url(r'^detalhe/$', views.pessoa_detalhe, name='Detalhe'),
    url(r'^sobre/', views.pessoa_sobre, name='Sobre'),
    url(r'^cadastro/$', views.cadastrar_usuario, name='Cadastro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

