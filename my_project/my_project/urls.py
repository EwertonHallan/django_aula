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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    url('^$', RedirectView.as_view(url='/login/')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url('^account/', include('django.contrib.auth.urls')),
    url('^login/$', auth_views.LoginView.as_view(template_name='pessoa/login.html'), name='login'),
    url('sair/$', auth_views.LogoutView.as_view(), name='logout'),
    url('^alterar-minha-senha/$', auth_views.PasswordChangeView.as_view(template_name='pessoa/password.html'), name='alterar-senha'),
    url(r'^pessoa/', include('pessoa.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page