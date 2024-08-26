from django.db import models

from .user_model import User

class Task(models.Model):
    name=models.CharField(max_length=150)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    description=models.CharField(max_length=1000)
    assigned_to=models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name} {self.start_date}"