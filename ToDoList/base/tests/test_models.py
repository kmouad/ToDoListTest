from django.test import TestCase
from base.models import Task
from datetime import datetime

class TestModels(TestCase):
    def setUp(self):
        self.todo = Task.objects.create(
            title='sample task to test',
            description='',
            finished=False,
            timeCreation=datetime.now()
        )

    def test_Task_creation(self):
        task = self.todo
        self.assertTrue(isinstance(task, Task))
        self.assertEqual(task.title, 'sample task to test')
        self.assertEqual(task.finished, False)