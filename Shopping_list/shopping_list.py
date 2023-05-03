lista_compras = []

# Imprimindo os comandos ao usuário
print("----------- Lista de compras -----------\n")
In_out = int(input("Inserir item [1]\n"
                   "Remover item [2]\n"
                   "Tirar valores duplicados [3]\n"
                   "Ordenar a lista [4]\n"
                   "Informar lista [5]\n"
                   "Limpar lista [6]\n"
                   "Parar programa[7]\n\n"
                   "Insira alguma opção: "))
# Verificando se a opção do usuário é valida
while In_out not in [1, 2, 3, 4, 5, 6, 7]:
    In_out = int(input("Insira alguma opção válida: "))

while In_out != 7:
    match In_out:
        # Inserir algo na lista
        case 1:
            valor = input("Insira: ")
            lista_compras.append(valor)

        # Remover algo da lista
        case 2:
            removendo = int(input("\n\tDeseja remover o item com o:"
                              "\n\t nome do item [1] "
                              "\n\t index do item [2] "
                              "\n\t Insira uma opção: "))
            while removendo not in [1, 2]:
                removendo = int(input("Insira alguma opção válida: "))

            # Remover com o nome (chave)
            if removendo == 1:
                valor = input("O que você deseja remover? ")
                if valor in lista_compras:
                    lista_compras.remove(valor)
                    print("Item removido com sucesso!")
                else:
                    print("Item não encontrado!")
            # Remover com a posição (index)
            elif removendo == 2:
                valor = int(input("Qual index você deseja remover? "))
                if valor in range(len(lista_compras)):
                    lista_compras.pop(valor+1)
                    print("Index removido com sucesso")
                else:
                    print("Index não encontrado!")
        # Tirar itens duplicados   
        case 3:
            ...
        # Ordenar a lista
        case 4: 
            ...
        # Imprime a lista
        case 5:
            print("Sua lista de compras consiste em: ")
            for i in lista_compras:
                print(i)
                
        # Limpar lista
        case 6: 
            ...
        # Pare o programa
        case 7:
            ...

    print()
    In_out = int(input("Inserir item [1]\n"
                       "Remover item [2]\n"
                       "Tirar valores duplicados [3]\n"
                       "Ordenar a lista [4]\n"
                       "Mostrar lista [5]\n"
                       "Limpar lista [6]\n"
                       "Parar programa[7]\n\n"
                       "Insira alguma opção: "))
    # Verificando se a opção do usuário é valida
    while In_out not in [1, 2, 3, 4, 5, 6, 7]:
        In_out = input("Insira alguma opção válida: ")


