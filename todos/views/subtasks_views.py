from django.shortcuts import render

from todos.models import Subtask

# Create your views here.

def subtasks_view(request):
    subtasks = Subtask.objects.all()

    context= {
        "subtasks": subtasks,
        "titulo": "Hola estamos proando el contexto"
    }

    return render(request, "subtasks/subtasks.html", context)