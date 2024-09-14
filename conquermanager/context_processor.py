from datetime import datetime

from conquermanager.settings import CLAVE, COLOR
from todos.models.subtask_model import Subtask
from todos.models.task_model import Task

def get_current_year_context_processor(request):
    current_year=datetime.now().year
    #Devolvemos un diccionario en lugar de devolver la variable directamente
    return {
        'current_year': current_year
    }

def get_statistics_todos(request):
    return {
        'n_tasks': Task.objects.all().count(),
        'n_subtasks': Subtask.objects.all().count()
    }

def get_clave(request):
    return {
        'clave': CLAVE,
        'color': COLOR
    }