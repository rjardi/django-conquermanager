from django.urls import path

from .views import subtasks_view, tasks_view, users_view

app_name = "todos"

urlpatterns = [
    path("tasks/", tasks_view, name="tasks_list"),
    path("subtasks/", subtasks_view, name="subtasks_list"),
    path("users/", users_view, name="users_list"),
]