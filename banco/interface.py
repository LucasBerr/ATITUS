def interface_do_usuario():

    print('###### - BEM VINDO AO BANCO DA CC - ######')
    
    print('2 - B')
    
    print("""
        1 - Criar nova conta
        2 - Buscar uma conta
        3 - Atualizar uma conta
        4 - Deletar uma conta
         
          """)
    
    escolha = int(input("Digite a sua escolha:"))
    
    while escolha > 4 and escolha < 1:
        escolha = int(input("Digite uma escolha válida"))
    
    
    match escolha:
        case 1:
            criar_conta_interface()
            
            
        case 2:
            buscar_conta_interface()
        
        case 3:
            atualizar_conta_interface()

        case 4:
            deletar_conta_interface()
            


def criar_conta_interface():
            nome_usuario = input("Digite o nome da pessoa que deseja cadastrar: ")
            email_correntista = input(f"Digite o email de {nome_usuario}: ")
            cpf = input(f"Digite o CPF de {nome_usuario}: ")
            limite = input("Digite o limite que deseja conceder ao correntista: ")
            
            criar_conta(nome = nome_usuario,limite = limite,cpf = cpf,email_correntista = email_correntista)
            


def buscar_conta_interface():
    print("""
            1 - Buscar conta por usuário
            2 - Buscar conta por nome
            3 - Buscar conta por cpf    
            """)
    
    escolha = int(input("Digite a sua escolha:"))
    
    while escolha > 3 and escolha < 1:
        escolha = int(input("Digite uma escolha válida"))
    
    match escolha:
        case 1:
            escolha_busca = input("Digite o id do usuário que deseja buscar:")
            busca = buscar_conta(usuario_id = escolha_busca)
            
            
           
        
        case 2:
            nome = input("Digite o nome do correntista que deseja buscar:")
            busca = buscar_conta(nome = escolha_busca)
            
       
            
        case 3:
            escolha_busca = input("Digite o cpf do correntista que deseja buscar:")
            busca = buscar_conta(cpf = escolha_busca)
      
            
    if busca == None:
        print("Usuário não encontrado!")
        return "Usuário não encontrado!"
    
    else:
        print(busca)
        return busca      
            
def atualizar_conta_interface():
    
    print("Escolha a conta que deseja atualizar!")
    
    conta = buscar_conta_interface()
    
    escolha = input("Essa foi a conta desejada?")
    
    while escolha == 'n' or conta == 'Usuário não encontrado!':
        buscar_conta_interface()
    
        escolha = input("Essa foi a conta desejada?")
        
    

    print("""
            1 - Atualizar o limite da conta
            2 - Atualizar o saque da conta
            3 - Atualizar o depósito da conta
            """)
    
    escolha = int(input("Digite a sua escolha:"))
    
    while escolha > 3 and escolha < 1:
        escolha = int(input("Digite uma escolha válida"))
        
        
        match escolha:
            case 1:
                limite = input("Digite o novo limite da conta: ")
                atualizar_conta(conta = conta, tipo = 'limite', troca = limite)
            
            case 2:
                saque = input("Digite o valor que deseja sacar na conta:")
                atualizar_conta(conta = conta, tipo = 'saque', troca = saque)
                
            case 3:
                deposito = input('Digite o valor que deseja depositar na conta:')
                atualizar_conta(conta = conta, tipo = 'deposito', troca = deposito)
                        



def deletar_conta_interface():
    print("Escolha a conta que deseja deletar!")
    buscar_conta_interface()