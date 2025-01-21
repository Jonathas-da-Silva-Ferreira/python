from django import initialize_django

def main_menu():
    """
    Menu principal para executar diferentes funções
    """
    print("Bem vindo ao sistema To-Do List")
    print("Escolha uma opção:")
    print("1: Iniciar Servidor Django")
    print("2: Rodar Migrações")
    print("3: Sair")
    choice = input("Digite o número da opção desejada: ")
    
    if choice == "1":
        initialize_django(runserver=True)
    elif choice == "2":
        initialize_django(migrate=True)
    elif choice == "3":
        print("Até mais!")
    else:
        print("Opção inválida")
        main_menu()

    if __name__ == "__main__":
        main_menu()
    
