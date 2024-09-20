from django.http import HttpResponse
from django.shortcuts import render

from core.models import Contact
from todos.forms.search_form import SearchForm
from todos.models import Task, Subtask
from django.core.mail import send_mail
from django.contrib import messages

from django.utils.translation import gettext as _


def helloworld(request):
    return HttpResponse("Holaaa") 

def home_view(request):
    messages.info(request,_('Este es un mensaje de Información'))
    return render(request,'main/home.html')

def search_view(request):
    search_form=SearchForm()
    context={
        'search_form': search_form
    }
    if request.GET:

        search_form=SearchForm(request.GET)
        search_string= search_form.data['search_string']

        tasks=Task.objects.filter(name__icontains=search_string)
        subtasks=Subtask.objects.filter(name__icontains=search_string)

        context={
            'tasks': tasks,
            'subtasks': subtasks,
            'search_form': search_form
        }
        return render(request, 'main/search.html', context)

    return render(request, "main/search.html", context)