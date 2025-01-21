import os
import sys
from django.core.management import execute_from_command_line

def initialize_djgando():
    """
    Inicializa o ambiente do Django para o projeto
    
    """

    #Defina o ambiente do Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_project.settings")

    #Executa migrações e inicilizar o servidor
    try:
        execute_from_command_line(['manage.py', 'migrate'])
        execute_from_command_line(['manage.py', 'runeserver'])
    except Exception as e:
        print(f"Erro ao inicializar o servidor Django: {e}")
        sys.exit(1)