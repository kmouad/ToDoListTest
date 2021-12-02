from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.urls import reverse_lazy


# View to list To Do tasks
class TasksList(ListView):
    model = Task
    context_object_name = 'tasks'

# View Set to use for viewing API results
class TasksSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#View to edit a To Do Task
class TaskUpdate(UpdateView):
    model = Task
    # Here we can choose wich field to edit, we will keep all fields so that we can change them
    fields = '__all__'
    success_url = reverse_lazy('tasks')



