from django.urls import path

from todos.views.tasks_views import TaskCreateView, TaskDeleteView, TaskDetail, TaskList, TaskUpdateView

app_name = "task"

urlpatterns = [
    path("list/", TaskList.as_view(), name="list"),
    path("detail/<pk>", TaskDetail.as_view(), name="detail"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("update/<pk>/", TaskUpdateView.as_view(), name="update"),
    path("delete/<pk>/", TaskDeleteView.as_view(), name="delete"),
]