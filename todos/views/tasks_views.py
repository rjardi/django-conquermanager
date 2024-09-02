from django.shortcuts import render

from todos.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tasks_view(request):
    tasks = Task.objects.all()

    context= {
        "tasks": tasks,
        "titulo": "Hola estamos proando el contexto"
    }

    return render(request, "tasks/tasks.html", context)