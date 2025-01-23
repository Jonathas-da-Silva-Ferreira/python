from django import initialize_django

def main_menu():
    """
    Menu principal para executar diferentes ações.
    """
    print("Bem-vindo ao sistema To-Do List!")
    print("Escolha uma opção:")
    print("1. Iniciar servidor Django")
    print("2. Rodar migrações")
    print("3. Sair")
    choice = input("Digite o número da opção: ")

    if choice == "1":
        initialize_django(runserver=True)
    elif choice == "2":
        initialize_django(migrate_only=True)
    elif choice == "3":
        print("Saindo...")
    else:
        print("Opção inválida!")
        main_menu()

if __name__ == "__main__":
    main_menu()