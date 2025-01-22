from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwenr

class TaskDetailView(ApiView):
    permission_classes = [IsAuthenticated, IsOwenr]

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)