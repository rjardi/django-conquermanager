from django.db import models

from .user_model import User
from .task_model import Task

class Subtask(models.Model):
    name=models.CharField(max_length=150)
    start_date=models.DateTimeField(null=True, blank=True)
    end_date=models.DateTimeField(null=True, blank=True)
    description=models.CharField(max_length=1000, null=True, blank=True)
    assigned_to=models.ManyToManyField(User)
    parent_task=models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} {self.start_date}"