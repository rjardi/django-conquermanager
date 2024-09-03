from django.db import models

from .user_model import User

class Task(models.Model):
    name=models.CharField(max_length=150)
    start_date=models.DateTimeField(null=True, blank=True)
    end_date=models.DateTimeField(null=True, blank=True)
    description=models.CharField(null=True, blank=True, max_length=1000)
    assigned_to=models.ManyToManyField(User)

    def __str__(self):
        return f"{self.name} {self.start_date}"