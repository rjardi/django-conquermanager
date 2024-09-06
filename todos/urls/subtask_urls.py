from django.urls import path

from todos.views.subtasks_views import SubTaskCreateView, SubTaskDeleteView, SubTaskDetail, SubTaskList, SubTaskUpdateView

app_name = "subtask"

urlpatterns = [
    path("list/", SubTaskList.as_view(), name="list"),
    path("detail/<pk>", SubTaskDetail.as_view(), name="detail"),
    path("create/", SubTaskCreateView.as_view(), name="create"),
    path("update/<pk>/", SubTaskUpdateView.as_view(), name="update"),
    path("delete/<pk>/", SubTaskDeleteView.as_view(), name="delete"),
]