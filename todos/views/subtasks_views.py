from django.shortcuts import render

from todos.models import Subtask
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def subtasks_view(request):
    subtasks = Subtask.objects.all()

    context= {
        "subtasks": subtasks,
        "titulo": "Hola estamos proando el contexto"
    }

    return render(request, "subtasks/subtasks.html", context)