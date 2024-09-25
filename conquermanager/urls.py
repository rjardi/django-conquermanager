"""conquermanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include, re_path

from conquermanager.views import SetLanguageView, helloworld, home_view, search_view
from core.views import ContactFormView, Prueba, PruebaTemplateView, contact_view, login_view, logout_view, register_view
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.i18n import i18n_patterns

# Prueba para demostrat como funcionan las path


urlpatterns = [
    re_path(r'^rosetta/', include('rosetta.urls')),
    path('set-language/', SetLanguageView.as_view(), name='set_language'),
    path('', home_view, name="home"),
    path('task/', include("todos.urls.task_urls", namespace="task")),
    path('subtask/', include("todos.urls.subtask_urls", namespace="subtask")),
    path('search/', search_view, name="search"),
    path('contact/ccbv/',ContactFormView.as_view(), name="contact_ccbv"),
    path('contact/',contact_view, name="contact"),
    path('admin/', admin.site.urls),
    # helloworld sera la función que resolverà la respuesta a la path /saludo
    path('saludo/', helloworld),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("prueba/", Prueba.as_view(), name="prueba"),
    path("pruebatemplateview/", PruebaTemplateView.as_view(), name="prueba_template_view"),
] + debug_toolbar_urls()

urlpatterns += i18n_patterns(
    path("buscar/", search_view, name="search"),
)
