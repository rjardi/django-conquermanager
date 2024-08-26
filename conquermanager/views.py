from django.http import HttpResponse
from django.shortcuts import render

from .models import Contact
from .forms import ContactForm
from todos.forms.search_form import SearchForm
from todos.models import Task, Subtask
from django.core.mail import send_mail


def helloworld(request):
    return HttpResponse("Holaaa") 

def home_view(request):
    return render(request,'main/home.html')

def contact_view(request):

    if request.POST:
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():

            name=contact_form.cleaned_data["name"]
            email=contact_form.cleaned_data["email"]
            message=contact_form.cleaned_data["message"]

            message_content=f"Se ha enviado correctamente de {name} con el correo {email} el mensaje: {message}"
            print(message_content)

            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            success=send_mail(
                "Probando",
                message_content,
                "from@example.com",
                ["to@example.com"],
                fail_silently=False,
            )

            context={
                "contact_form": contact_form,
                'success': success
            }            
            return render(request,'main/contact.html', context)

    
    contact_form=ContactForm()
    context={
        "contact_form": contact_form
    }

    return render(request,'main/contact.html', context)

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