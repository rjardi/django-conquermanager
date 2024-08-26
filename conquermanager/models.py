from django.utils import timezone
from django.db import models

class Contact(models.Model):

    name=models.CharField(
        verbose_name='Nombre', 
        max_length=50
        )
    
    email=models.EmailField(
        verbose_name="Email"
        )
    
    message=models.TextField(
        verbose_name="Mensaje enviado"
        )
    
    created_at=models.DateTimeField(
        verbose_name='Fecha y hora de creación',
        default=timezone.now
        )
    
    def __str__(self):
        return self.name
    