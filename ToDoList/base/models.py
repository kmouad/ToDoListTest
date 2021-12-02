from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

# Create your models here.
# Model class for all to do tasks
class Task(models.Model):
    # delete all tasks if user deleted
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    # title mandatory
    title = models.CharField(max_length=200)
    # description optional
    description = models.TextField(null=True, blank=True)
    # status of the task
    finished = models.BooleanField(default=False)
    # Creation time of the task, will be used to order our To Do tasks
    timeCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # Ordering by status first and secondly by time creation
    #The last task created first
    class Meta:
        ordering = ['finished', F('timeCreation').desc()]
