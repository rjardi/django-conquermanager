from django.views.generic import ListView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from todos.decorators import user_can_delete_task
from todos.forms.task_form import TaskCreate, TaskModelFormCreate
from todos.models import Task
from django.views.generic import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class TaskList(ListView):
    model=Task
    template_name='tasks/tasks_list.html'
    context_object_name='tasks'

class TaskDetail(DetailView):
    model=Task
    template_name='tasks/task_detail.html'
    context_object_name='task'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo']='Este es mi titulo'
        return context
    
@method_decorator(login_required, name='dispatch')    
class TaskCreateView(CreateView):
    model = Task
    # fields = [
    #     "name",
    #     'start_date',
    #     'end_date',
    #     'description'
    # ]
    form_class=TaskModelFormCreate    
    template_name='tasks/task_create.html'
    success_url=reverse_lazy('task:list')

    def form_valid(self,form):
        form.instance.created_by=self.request.user
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = Task
    fields = [
        "name",
        'start_date',
        'end_date',
        'description'
    ]    
    template_name='tasks/task_update.html'
    success_url=reverse_lazy('task:list')

@method_decorator(user_can_delete_task, name='dispatch')
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task:list")
    template_name='tasks/task_delete.html'

# Create your views here.
@login_required
def tasks_view(request):
    tasks = Task.objects.all()

    context= {
        "tasks": tasks,
        "titulo": "Hola estamos probando el contexto"
    }

    return render(request, "tasks/tasks.html", context)

@login_required
def task_create(request):
    if request.POST:
        form=TaskModelFormCreate(request.POST)
        if form.is_valid():
            new_task=Task.objects.create(
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                description=form.cleaned_data['description'],
            )
            #Redireccionar a la vista detalle de la nueva tarea creada
            return redirect(reverse('todos:task_detail', kwargs={'id':new_task.pk}))
    else:
        form=TaskModelFormCreate()

    context={
        'form': form
    }
    return render(request, 'tasks/task_create.html', context)

def task_detail(request, id):
    task=Task.objects.get(pk=id)
    context={
        'task':task
    }
    return render(request, "tasks/task_detail.html", context)