"""musica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from imusica.views import *
from imusica.models import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$',mainpage),

    url(r'^admin/',include(admin.site.urls)),
    url(r'^app/', include('imusica.urls', namespace='imusica')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name = 'logout'),

]
