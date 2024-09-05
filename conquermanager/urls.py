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
from django.urls import path, include

from conquermanager.views import helloworld, home_view, search_view
from core.views import ContactFormView, Prueba, PruebaTemplateView, contact_view, login_view, logout_view, register_view

# Prueba para demostrat como funcionan las path


urlpatterns = [
    path('', home_view, name="home"),
    path('', include("todos.urls", namespace="todos")),
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
]
