from django.contrib import admin

# Register your models here.
from todos.models import Task, Subtask, User

class SubTaskInline(admin.TabularInline):
    model=Subtask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=["name", "start_date", "end_date", "description"]
    list_filter=["name"]
    search_fields=["name"]
    # Relation field many to many
    filter_horizontal=("assigned_to", )
    # Relation field One to Many
    inlines=[
        SubTaskInline
    ]

@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display=["name", "start_date", "end_date", "description", "parent_task"]
    list_filter=["name"]
    search_fields=["name"]

@admin.register(User)   
class UserAdmin(admin.ModelAdmin):
    list_display=["first_name", "last_name"]
    list_filter=["first_name"]
    search_fields=["first_name"]
