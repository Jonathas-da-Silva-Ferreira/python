from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Permissão customizada para garantir que apenas o dono da tarefa tenha acesso.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user