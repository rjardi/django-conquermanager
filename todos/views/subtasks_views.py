from django.shortcuts import render
from django.urls import reverse_lazy

from todos.models import Subtask
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class SubTaskList(ListView):
    model=Subtask
    template_name='subtasks/subtasks_list.html'
    context_object_name='subtasks'

class SubTaskDetail(DetailView):
    model=Subtask
    template_name='subtasks/subtask_detail.html'
    context_object_name='subtask'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Este es mi titulo'
        return context
    
class SubTaskCreateView(CreateView):
    model = Subtask
    fields = [
        "name",
        'start_date',
        'end_date',
        'description'
    ]    
    template_name='subtasks/subtask_create.html'
    success_url=reverse_lazy('subtask:list')

class SubTaskUpdateView(UpdateView):
    model = Subtask
    fields = [
        "name",
        'start_date',
        'end_date',
        'description'
    ]    
    template_name='subtasks/subtask_update.html'
    success_url=reverse_lazy('subtask:list')

class SubTaskDeleteView(DeleteView):
    model = Subtask
    success_url = reverse_lazy("subtask:list")
    template_name='subtasks/subtask_delete.html'

# Create your views here.
@login_required
def subtasks_view(request):
    subtasks = Subtask.objects.all()

    context= {
        "subtasks": subtasks,
        "titulo": "Hola estamos proando el contexto"
    }

    return render(request, "subtasks/subtasks.html", context)