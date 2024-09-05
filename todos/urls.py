from django.urls import path

from todos.views.tasks_views import TaskDetail, TaskList, task_create, task_detail

from .views import subtasks_view, tasks_view, users_view

app_name = "todos"

urlpatterns = [
    path("tasks/", tasks_view, name="tasks_list"),
    path("tasks/create/", task_create, name="task_create"),
    path("tasks/detail/<int:id>", task_detail, name="task_detail"),
    path("subtasks/", subtasks_view, name="subtasks_list"),
    path("users/", users_view, name="users_list"),
    path("tasks/list", TaskList.as_view(), name="tasks_list_ccbv"),
    path("tasks/detail/ccbv/<pk>", TaskDetail.as_view(), name="task_detail_ccbv"),
 
]