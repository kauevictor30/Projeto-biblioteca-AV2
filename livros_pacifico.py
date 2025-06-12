def adicionar_livro(titulo, autor, ano_publicacao, novo_id):
    livro = {
        'id': novo_id,
        'titulo': titulo,
        'autor': autor,
        'ano_publicacao': ano_publicacao,
        'disponivel': True
    }
    print(f"Livro '{titulo}' adicionado com sucesso!")
    return livro

def listar_livros(catalogo_de_livros):
    if not catalogo_de_livros:
        print('Nenhum livro foi encontrado no catálogo.')
        return
    for livro in catalogo_de_livros:
        status = "Disponível" if livro['disponivel'] else "Emprestado"
        print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {status}")

def buscar_livro_por_titulo(catalogo_de_livros, titulo_busca):
    encontrou_algum = False
    for livro in catalogo_de_livros:
        if titulo_busca.lower() in livro['titulo'].lower():
            print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
            encontrou_algum = True
    if not encontrou_algum:
        print('Nenhum livro encontrado com esse título.')

def atualizar_disponibilidade_livro(catalogo_de_livros, id_livro, disponivel):
    livro_encontrado = None
    for livro in catalogo_de_livros:
        if livro['id'] == id_livro:
            livro_encontrado = livro
            break
            
    if not livro_encontrado:
        print("Erro: Livro não encontrado.")
        return False
        
    livro_encontrado['disponivel'] = disponivel
    status_texto = "Disponível" if disponivel else "Indisponível (Emprestado)"
    print(f"Disponibilidade do livro ID {id_livro} atualizada para: {status_texto}.")
    return True