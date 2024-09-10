

from django.http import Http404
from todos.models.task_model import Task
from django.core.exceptions import PermissionDenied


def user_can_delete_task(function):
  
    def wrap(request, *args, **kwargs):
        
        try:
            task=Task.objects.get(pk=kwargs['pk'])
        except Task.DoesNotExist:
            raise Http404
        if request.user == task.created_by:
            return(function(request, *args, **kwargs))

        raise PermissionDenied

    return wrap