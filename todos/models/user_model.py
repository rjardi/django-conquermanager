from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
