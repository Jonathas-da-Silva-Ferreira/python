from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner  # Permissão customizada

class TaskDetailView(APIView):
    """
    Classe para visualizar os detalhes de uma tarefa específica.
    Permite acesso somente ao proprietário da tarefa.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, pk):
        # Obtém a tarefa ou retorna 404 se não for encontrada
        task = get_object_or_404(Task, pk=pk)
        # Verifica as permissões para o objeto (se o usuário é o proprietário)
        self.check_object_permissions(request, task)
        # Serializa a tarefa e retorna os dados como resposta
        serializer = TaskSerializer(task)
        return Response(serializer.data)