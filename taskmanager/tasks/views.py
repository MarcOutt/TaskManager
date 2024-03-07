from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from . import models, forms


class TaskView(View):
    """ Permet d'afficher les tâches en cours """
    template_name = 'task/home.html'

    def get(self, request):
        tasks = models.Task.objects.all()
        return render(request, self.template_name, context={'tasks': tasks})


class CreateTaskView(CreateView):
    model = models.Task
    template_name = 'task/task_form.html'
    form_class = forms.TaskForm
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        task_form = self.form_class()
        return render(request, self.template_name, context={'task': task_form})

    def post(self, request, *args, **kwargs):
        task_form = forms.TaskForm(request.POST, request.FILES)
        if task_form.is_valid():
            task_form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, context={'task': task_form})
