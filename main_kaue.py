import json
from menu_gui import menu
from livros_pacifico import adicionar_livro, listar_livros, buscar_livro_por_titulo, atualizar_disponibilidade_livro
from usuarios_sara import adicionar_usuario, listar_usuarios, buscar_usuario_por_id, altera_email
from emprestimos_taina import realizar_emprestimo, devolver_livro, listar_emprestimos_ativos, historico_emprestimos_usuario

try:
    with open('livros.json', 'r', encoding='utf-8') as f:
        catalogo_livros = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    catalogo_livros = []

try:
    with open('usuarios.json', 'r', encoding='utf-8') as f:
        cadastro_usuarios = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    cadastro_usuarios = []

try:
    with open('emprestimos.json', 'r', encoding='utf-8') as f:
        registros_emprestimos = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    registros_emprestimos = []


while True:
    menu()
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print("\nERRO: Digite apenas números!\n")
        continue

    if opcao == 1:
        print("\n--- Adicionar Novo Livro ---")
        nome_livro = input('Qual o nome do livro? ')
        autor_livro = input('Qual o autor do livro? ')
        ano_publicacao = input('Qual o ano de publicação? ')
        
        if not catalogo_livros:
            novo_id = 1
        else:
            novo_id = catalogo_livros[-1]['id'] + 1

        novo_livro = adicionar_livro(nome_livro, autor_livro, ano_publicacao, novo_id)
        catalogo_livros.append(novo_livro)
        
        with open('livros.json', 'w', encoding='utf-8') as f:
            json.dump(catalogo_livros, f, indent=4, ensure_ascii=False)
        print("Dados dos livros salvos com sucesso!")

    elif opcao == 2:
        print("\n--- Catálogo de Livros ---")
        listar_livros(catalogo_livros)

    elif opcao == 3:
        print("\n--- Buscar Livro por Título ---")
        titulo_para_buscar = input('Digite o título do livro que deseja buscar: ')
        buscar_livro_por_titulo(catalogo_livros, titulo_para_buscar)

    elif opcao == 4:
        print("\n--- Atualizar Disponibilidade de Livro ---")
        try:
            id_livro = int(input("Digite o ID do livro: "))
            status_input = input("O livro está disponível? (s/n): ").lower()
            if status_input == 's':
                disponivel = True
            elif status_input == 'n':
                disponivel = False
            else:
                raise ValueError("Resposta inválida.")
            sucesso = atualizar_disponibilidade_livro(catalogo_livros, id_livro, disponivel)
            if sucesso:
                with open('livros.json', 'w', encoding='utf-8') as f:
                    json.dump(catalogo_livros, f, indent=4, ensure_ascii=False)
                print("Dados dos livros salvos com sucesso!")
        except ValueError:
            print("Entrada inválida. O ID deve ser um número e a resposta deve ser 's' ou 'n'.")

    elif opcao == 5:
        print("\n--- Adicionar Novo Usuário ---")
        nome_usuario = input("Digite o nome do usuário: ")
        while True:
            email_usuario = input("Digite o email do usuário: ")
            email_existente = False
            for u in cadastro_usuarios:
                if u['email'] == email_usuario:
                    email_existente = True
                    break
            if email_existente:
                print("ERRO: Este email já está em uso. Por favor, digite outro.")
            else:
                break
        
        if not cadastro_usuarios:
            novo_id = 1
        else:
            novo_id = cadastro_usuarios[-1]['id'] + 1
            
        novo_usuario = adicionar_usuario(nome_usuario, email_usuario, novo_id)
        cadastro_usuarios.append(novo_usuario)
        
        with open('usuarios.json', 'w', encoding='utf-8') as f:
            json.dump(cadastro_usuarios, f, indent=4, ensure_ascii=False)
        print("Dados de usuários salvos com sucesso!")

    elif opcao == 6:
        print("\n--- Lista de Usuários ---")
        listar_usuarios(cadastro_usuarios)
    
    elif opcao == 7:
        print("\n--- Buscar Usuário por ID ---")
        try:
            id_usuario = int(input("Digite o ID do usuário a ser buscado: "))
            buscar_usuario_por_id(cadastro_usuarios, id_usuario)
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    elif opcao == 8:
        print("\n--- Alterar Email de Usuário ---")
        try:
            id_usuario = int(input("Digite o ID do usuário: "))
            novo_email = input("Digite o novo email: ")
            sucesso = altera_email(cadastro_usuarios, id_usuario, novo_email)
            if sucesso:
                with open('usuarios.json', 'w', encoding='utf-8') as f:
                    json.dump(cadastro_usuarios, f, indent=4, ensure_ascii=False)
                print("Dados de usuários salvos com sucesso!")
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    elif opcao == 9:
        print("\n--- Realizar Empréstimo ---")
        try:
            id_livro = int(input('Digite o ID do livro: '))
            id_usuario = int(input('Digite o ID do usuário: '))
            sucesso = realizar_emprestimo(registros_emprestimos, catalogo_livros, cadastro_usuarios, id_livro, id_usuario)
            if sucesso:
                with open('emprestimos.json', 'w', encoding='utf-8') as f:
                    json.dump(registros_emprestimos, f, indent=4, ensure_ascii=False)
                with open('livros.json', 'w', encoding='utf-8') as f:
                    json.dump(catalogo_livros, f, indent=4, ensure_ascii=False)
                print("Dados de empréstimos e livros salvos com sucesso!")
        except ValueError:
            print("IDs inválidos. Por favor, digite números.")

    elif opcao == 10:
        print("\n--- Devolver Livro ---")
        try:
            id_emprestimo = int(input('Digite o ID do empréstimo a ser devolvido: '))
            sucesso = devolver_livro(registros_emprestimos, catalogo_livros, id_emprestimo)
            if sucesso:
                with open('emprestimos.json', 'w', encoding='utf-8') as f:
                    json.dump(registros_emprestimos, f, indent=4, ensure_ascii=False)
                with open('livros.json', 'w', encoding='utf-8') as f:
                    json.dump(catalogo_livros, f, indent=4, ensure_ascii=False)
                print("Dados de empréstimos e livros salvos com sucesso!")
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    elif opcao == 11:
        print("\n--- Empréstimos Ativos ---")
        listar_emprestimos_ativos(registros_emprestimos, catalogo_livros, cadastro_usuarios)

    elif opcao == 12:
        print("\n--- Histórico de Empréstimos por Usuário ---")
        try:
            id_usuario = int(input('Digite o ID do usuário: '))
            historico_emprestimos_usuario(registros_emprestimos, catalogo_livros, id_usuario)
        except ValueError:
            print("ID inválido. Por favor, digite um número.")

    elif opcao == 13:
        print("\nSaindo do programa. Até mais!")
        break
    
    else:
        print("\nERRO: Opção inválida. Tente novamente.\n")


# sistema feito por:
# kauê victor --> main
# sara beatriz --> usuarios
# tainá miranda --> emprestimos
# guilherme nascimento --> menu
# matheus pacifico --> livros