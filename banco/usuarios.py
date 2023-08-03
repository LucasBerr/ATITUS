from dados import *

"""
GESTAO DA CONTA:
criar_conta()
buscar_conta()
atualizar_conta()
deletar_conta()
"""

def criar_conta(nome, limite, cpf, email_correntista):
    nome_usuario = nome
    limite_usuario = float(limite)
    email_correntista = email_correntista

    # Criar um novo usuário
    novo_usuario = {
                "nome": nome_usuario,
                "saldo": "0",
                "limite": limite_usuario,
                "cpf": cpf,
                "email_correntista": email_correntista        
                }
    
    # pegar os dados do banco
    usuarios = ler_arquivo()

    if usuarios == 1:
        guardar_arquivo({0: novo_usuario,})
    else:
        # Calcular ID
        id = len(usuarios)


        # Adiciona o usuário na base         
        usuarios[id] = novo_usuario 

        # Atualiza a base de dados
        guardar_arquivo(usuarios)



def buscar_conta(usuario_id="-1", nome="nenhum", cpf="nenhum"):
    
    # Ler arquivo
    dados = ler_arquivo()
    if dados == 1:
        print("Nenhum usuário dentro do banco")
        return
    
    # Verificando qual opcao de busca o corretor selecionou
    if usuario_id != "-1":
        usuario_selecionado = buscar_conta_por_id(usuario_id, dados)
    elif nome != "nenhum":
        usuario_selecionado = buscar_conta_por_nome(nome, dados)
    elif cpf != "nenhum":
        usuario_selecionado = buscar_conta_por_cpf(cpf, dados)

    return usuario_selecionado

def atualizar_conta(conta, tipo, troca):
    print(conta)



def buscar_conta_por_id(usuario_id, dados):
    usuario_encontrado = "-1"

    for id in dados:
        if id == usuario_id:
            usuario_encontrado = id
            
    if usuario_encontrado == "-1":
        return None
    else:
        return dados[id]
        
def buscar_conta_por_nome(nome, dados):
    usuario_encontrado = "-1"

    for id in dados:
        if dados[id]["nome"] == nome:
            usuario_encontrado = id

    if usuario_encontrado == "-1":
        return None
    else:
        return dados[id]
    

def buscar_conta_por_cpf(cpf, dados):
    usuario_encontrado = "-1"

    for id in dados:
        if dados[id]["cpf"] == cpf:
            usuario_encontrado = id

    if usuario_encontrado == "-1":
        return None


def dados_formatados_usuario(usuario):
    return f"""
nome : {usuario["nome"]}
saldo: {usuario["saldo"]}
limite: {usuario["limite"]}
cpf: {usuario["limite"]}
email correntista: {usuario["email_correntista"]}
"""
    s

buscar_conta(nome="Lucas Berr")
