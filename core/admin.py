from django.contrib import admin

# Register your models here.
from core.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model= Contact
    list_display=["name", "email", "message"]


