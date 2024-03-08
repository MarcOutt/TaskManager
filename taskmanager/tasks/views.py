from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class TaskListView(View):
    template_name = 'task/task_list.html'

    def get(self, request):
        tasks = models.Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks})


# CRUD Task
class CreateTaskView(CreateView):
    model = models.Task
    template_name = 'task/task_form.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy("home")


class TaskDetailView(DetailView):
    model = models.Task
    template_name = 'task/task_detail.html'


class TaskUpdateView(UpdateView):
    model = models.Task
    template_name = 'task/task_form.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy("home")


class TaskDeleteView(DeleteView):
    model = models.Task
    template_name = 'task/delete_task.html'
    success_url = reverse_lazy("home")



