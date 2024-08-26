from django.shortcuts import render

from todos.models import User

# Create your views here.

def users_view(request):
    users = User.objects.all()

    context= {
        "users": users,
        "titulo": "Hola estamos proando el contexto"
    }

    return render(request, "users/users.html", context)