from rest_framework.permissions import BasePermission

class IsOwenr(BasePermission):
    """
    Permissão customizadas para garantir que apenas o dono de tarefa tenha acesso.
    """

def has_object_permission(self, request, view, obj):
    return obj.user == request.user 
