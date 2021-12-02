from django.urls import path
from rest_framework import routers
from .views import TasksList, TasksSet


router = routers.DefaultRouter()
router.register('tasksSets', TasksSet)

urlpatterns = [
    path('', TasksList.as_view(), name='tasks'),
]