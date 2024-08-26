from django.shortcuts import render

from todos.models import Task

# Create your views here.

def tasks_view(request):
    tasks = Task.objects.all()

    context= {
        "tasks": tasks,
        "titulo": "Hola estamos proando el contexto"
    }

    return render(request, "tasks/tasks.html", context)