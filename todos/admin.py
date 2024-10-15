from django.contrib import admin

# Register your models here.
from todos.models import Task, Subtask

class SubTaskInline(admin.TabularInline):
    model=Subtask

# Definir la acción personalizada 
def set_tasks_done(modeladmin, request, queryset): 
    # Actualizar los objetos seleccionados a "publicados" 
    queryset.update(done=True) 
    # Mostrar un mensaje informativo en la interfaz de administracion 
    modeladmin.message_user(request, "Las tareas seleccionadas se han marcado como realizadas.") 

# Personalizar el nombre de la acción
set_tasks_done.short_description = "Marcar tareas como realizadas"

# Definir la acción personalizada para exportar a CSV
def export_tasks_to_csv(modeladmin, request, queryset) :
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response ['Content-Disposition'] = 'attachment; filename="tasks.csv"'
    writer = csv.writer(response)

    writer.writerow( ["name", "start_date", "end_date", "description", 'created_by', 'done'] )
    for task in queryset:
        writer.writerow( [task.name, task.start_date, task.end_date, task.description, task.created_by, task.done] )

    return response

# Personalizar el nombre de la acción
export_tasks_to_csv.short_description = "Exportar tareas seleccionados a CSV"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=["name", "start_date", "end_date", "description", 'created_by', 'done']
    list_filter=["name","done"]
    search_fields=["name"]
    # Relation field many to many
    # filter_horizontal=("created_by", )
    # Relation field One to Many
    inlines=[
        SubTaskInline
    ]
    actions=[set_tasks_done, export_tasks_to_csv]

@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display=["name", "start_date", "end_date", "description", "parent_task"]
    list_filter=["name"]
    search_fields=["name"]



