from rest_framework import  serializers
from .models import Task

# Here we serialize from our database to json and from json to our database
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'