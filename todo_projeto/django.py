import os
import sys
from django.core.management import execute_from_command_line

def initialize_django(runserver=False, migrate_only=False, env='development'):
    """
    Inicializa o ambiente Django para o projeto.
    
    Args:
        runserver (bool): Define se o servidor deve ser iniciado.
        migrate_only (bool): Define se apenas as migrações devem ser executadas.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"todo_project.settings.{env}")

    try:
        if migrate_only:
            print("Executando migrações...")
            execute_from_command_line(["manage.py", "migrate"])
            print("Migrações concluídas com sucesso!")
        elif runserver:
            print("Iniciando servidor Django...")
            execute_from_command_line(["manage.py", "runserver"])
        else:
            print("Nenhuma ação especificada.")
    except Exception as e:
        print(f"Erro ao inicializar o Django: {e}")
        sys.exit(1)
