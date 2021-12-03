from django.urls import path
from rest_framework import routers
from .views import TasksList, TasksSet, TaskUpdate, TaskDetail


router = routers.DefaultRouter()
router.register('tasksSets', TasksSet)

urlpatterns = [
    path('', TasksList.as_view(), name='tasks'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task')
]