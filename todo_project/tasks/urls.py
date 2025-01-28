from django.urls import path
from .views import TaskDetailView

urlpatterns = [
    # Rota para detalhes da tarefa
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]