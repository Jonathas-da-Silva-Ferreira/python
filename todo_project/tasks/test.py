from django.test import TestCase
from tasks.models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(title="Estudar Django")

    def test_task_creation(self):
        """Verifica se a tarefa foi criada corretamente."""
        self.assertEqual(self.task.title, "Estudar Django")