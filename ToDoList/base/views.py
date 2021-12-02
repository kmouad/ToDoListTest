from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


# View to list To Do tasks
class TasksList(ListView):
    model = Task
    context_object_name = 'tasks'
# View Set to use for viewing API results
class TasksSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


