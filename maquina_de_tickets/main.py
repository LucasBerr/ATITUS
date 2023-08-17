from maquina import Maquina

def main():
    preco_do_ticket = input("Preço do ticket em centavos: ")

    maquina = Maquina(preco_do_ticket)
    interface(maquina)

def interface(maquina: Maquina):
    menu = f"""
MÁQUINA DE TICKETS: [possuo {maquina.get_dinheiro_inserido()} centavos]
[a] Inserir Moedas
[b] Imprimir Ticket
[x] Encerrar Operação
    """
    print(menu)
    escolha = escolher(["a", "b", "x"])

    match escolha:
        case "a":
            inserir_moedas(maquina)
            interface(maquina)

        case "b":
            maquina.imprimir_ticket()
            interface(maquina)

        case "x":
            print(f"Total Arrecadado: {maquina.dinheiro_arrecadado()}")

def inserir_moedas(maquina:Maquina):
    moedas = 0
    moeda_do_usuário = 0
    while moeda_do_usuário != "-1":
        moeda_do_usuário = input("Informe a moeda [-1 para parar]: ")
        # Protegendo caso o usuário use uma letra
        try:
            if int(moeda_do_usuário) > 0:
                moedas += int(moeda_do_usuário)
        except ValueError:
            print("Não entendi a moeda que você colocou!")

    # adicionando dinheiro na máquina:
    maquina.inserir_dinheiro(moedas)






def escolher(alternativas):
    escolha = input("Digite a sua escolha: ")

    while escolha not in alternativas:
        escolha = input("Digite uma escolha válida: ")

    return escolha


if __name__ == "__main__":
    main()