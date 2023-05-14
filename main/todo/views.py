from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TodoAction():
    
    def create():
        return TaskCreateView.as_view()
    
    def read():
        return TaskListView.as_view()
    
    def update():
        return TaskUpdateView.as_view()
    
    def delete():
        return TaskDeleteView.as_view()

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home"
        return context

task_list_url = reverse_lazy('task_list')


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_error'] = getattr(self, 'title_error', None)
        context['title'] = "Add Task"
        return context
    
    def form_valid(self, form):

        if len(form.cleaned_data['title'])<3:
            self.title_error = 'Title must have at least 3 characters.!'
            return self.form_invalid(form)
        
        else:
            return super().form_valid(form)

task_create_url = reverse_lazy('task_create')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Update Task"
        return context

task_update_url = reverse_lazy('task_update', args=[1]) 

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete Task"
        return context

task_delete_url = reverse_lazy('task_delete', args=[1])  