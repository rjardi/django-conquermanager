from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):
    name=models.CharField(max_length=150)
    start_date=models.DateTimeField(null=True, blank=True)
    end_date=models.DateTimeField(null=True, blank=True)
    description=models.CharField(null=True, blank=True, max_length=1000)
    # assigned_to=models.ManyToManyField(User)
    created_by=models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    done=models.BooleanField("Tarea realizada",default=False)

    LEVEL_CHOICES ={
        "1":"Nivel 1",
        "2":"Nivel 2",
        "3":"Nivel 3"
    }

    level=models.CharField("Nivel", max_length=2, choices=LEVEL_CHOICES, default="1")

    def __str__(self):
        return f"{self.name} {self.start_date}"