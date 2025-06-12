from datetime import date

def realizar_emprestimo(registros_emprestimos, catalogo_livros, cadastro_usuarios, id_livro, id_usuario):
    livro_encontrado = None
    for livro in catalogo_livros:
        if livro['id'] == id_livro:
            livro_encontrado = livro
            break

    usuario_encontrado = None
    for usuario in cadastro_usuarios:
        if usuario['id'] == id_usuario:
            usuario_encontrado = usuario
            break

    if not livro_encontrado:
        print("Erro: Livro não encontrado.")
        return False
    if not usuario_encontrado:
        print("Erro: Usuário não encontrado.")
        return False
    if not livro_encontrado['disponivel']:
        print("Erro: Livro já está emprestado.")
        return False

    if not registros_emprestimos:
        novo_id_emprestimo = 1
    else:
        novo_id_emprestimo = registros_emprestimos[-1]['id'] + 1
        
    novo_emprestimo = {
        'id': novo_id_emprestimo,
        'id_livro': id_livro,
        'id_usuario': id_usuario,
        'data_emprestimo': date.today().strftime("%d-%m-%Y"),
        'data_devolucao': None
    }
    
    registros_emprestimos.append(novo_emprestimo)
    livro_encontrado['disponivel'] = False
    print('Empréstimo realizado com sucesso!')
    return True

def devolver_livro(registros_emprestimos, catalogo_livros, id_emprestimo):
    emprestimo_encontrado = None
    for emp in registros_emprestimos:
        if emp['id'] == id_emprestimo and emp['data_devolucao'] is None:
            emprestimo_encontrado = emp
            break

    if not emprestimo_encontrado:
        print('Erro: Empréstimo não encontrado ou já devolvido.')
        return False
    
    emprestimo_encontrado['data_devolucao'] = date.today().strftime("%d-%m-%Y")
    
    livro_devolvido = None
    for livro in catalogo_livros:
        if livro['id'] == emprestimo_encontrado['id_livro']:
            livro_devolvido = livro
            break
    
    if livro_devolvido:
        livro_devolvido['disponivel'] = True
    
    print('Livro devolvido com sucesso!')
    return True

def listar_emprestimos_ativos(registros_emprestimos, catalogo_livros, cadastro_usuarios):
    ativos = []
    for emp in registros_emprestimos:
        if emp['data_devolucao'] is None:
            ativos.append(emp)

    if not ativos:
        print("Nenhum empréstimo ativo no momento.")
        return

    for emprestimo in ativos:
        livro_emprestado = None
        for l in catalogo_livros:
            if l['id'] == emprestimo['id_livro']:
                livro_emprestado = l
                break
        
        usuario_emprestimo = None
        for u in cadastro_usuarios:
            if u['id'] == emprestimo['id_usuario']:
                usuario_emprestimo = u
                break

        nome_livro = livro_emprestado['titulo'] if livro_emprestado else "Livro Desconhecido"
        nome_usuario = usuario_emprestimo['nome'] if usuario_emprestimo else "Usuário Desconhecido"
        
        print(f"ID Empréstimo: {emprestimo['id']} | Livro: '{nome_livro}' com Usuário: '{nome_usuario}'")

def historico_emprestimos_usuario(registros_emprestimos, catalogo_livros, id_usuario):
    emprestimos_do_usuario = []
    for emp in registros_emprestimos:
        if emp['id_usuario'] == id_usuario:
            emprestimos_do_usuario.append(emp)

    if not emprestimos_do_usuario:
        print(f"Nenhum histórico de empréstimo encontrado para o usuário com ID {id_usuario}.")
        return
    
    print(f"--- Histórico do Usuário ID: {id_usuario} ---")
    for emprestimo in emprestimos_do_usuario:
        livro_emprestado = None
        for l in catalogo_livros:
            if l['id'] == emprestimo['id_livro']:
                livro_emprestado = l
                break
        
        nome_livro = livro_emprestado['titulo'] if livro_emprestado else "Livro Desconhecido"
        status = f"Devolvido em {emprestimo['data_devolucao']}" if emprestimo['data_devolucao'] else "Emprestado"
        print(f"Livro: '{nome_livro}' | Data Empréstimo: {emprestimo['data_emprestimo']} | Status: {status}")