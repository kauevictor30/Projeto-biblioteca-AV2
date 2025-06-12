def adicionar_usuario(nome, email, novo_id):
    usuario = {
        "id": novo_id,
        "nome": nome,
        "email": email
    }
    print(f"Usuário '{nome}' adicionado com sucesso!")
    return usuario

def listar_usuarios(lista_de_usuarios):
    if not lista_de_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("Lista de usuários:")
    for usuario in lista_de_usuarios:
        print(f"ID: {usuario['id']} | Nome: {usuario['nome']} | Email: {usuario['email']}")

def buscar_usuario_por_id(lista_de_usuarios, id_usuario):
    usuario_encontrado = None
    for u in lista_de_usuarios:
        if u['id'] == id_usuario:
            usuario_encontrado = u
            break
            
    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return None
        
    print(f"Usuário encontrado: ID: {usuario_encontrado['id']} | Nome: {usuario_encontrado['nome']} | Email: {usuario_encontrado['email']}")
    return usuario_encontrado

def altera_email(lista_de_usuarios, id_usuario, novo_email):
    usuario_encontrado = None
    for u in lista_de_usuarios:
        if u['id'] == id_usuario:
            usuario_encontrado = u
            break
            
    if not usuario_encontrado:
        print("Erro: Usuário não encontrado.")
        return False
    
    email_existente = None
    for u in lista_de_usuarios:
        if u['email'] == novo_email and u['id'] != id_usuario:
            email_existente = u
            break
            
    if email_existente:
        print("Erro: O novo email já pertence a outro usuário.")
        return False

    usuario_encontrado['email'] = novo_email
    print("Email alterado com sucesso!")
    return True