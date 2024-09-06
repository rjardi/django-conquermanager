from django.contrib import admin

# Register your models here.
from todos.models import Task, Subtask

class SubTaskInline(admin.TabularInline):
    model=Subtask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=["name", "start_date", "end_date", "description", 'created_by']
    list_filter=["name"]
    search_fields=["name"]
    # Relation field many to many
    # filter_horizontal=("created_by", )
    # Relation field One to Many
    inlines=[
        SubTaskInline
    ]

@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display=["name", "start_date", "end_date", "description", "parent_task"]
    list_filter=["name"]
    search_fields=["name"]


