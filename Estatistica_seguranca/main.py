import csv
import json

def main():
    print("\n============= Estatísticas de Segurança Pública =============\n")
    jan21 = []
    jan22 = []
    jan23 = []
    
    open_csv("./dados/jan-21.CSV", jan21)
    open_csv("./dados/jan-22.CSV", jan22)
    open_csv("./dados/jan-23.CSV", jan23)


    # Criando o dicionário consolidado de cada cidade 
    # chave = nome da cidade
    # valor = pontos que essa cidade tem em crimes
    ind_cid_violentos = {}
    ind_cid_n_violentos = {}

    consolid_dict([jan21, jan22, jan23], [ind_cid_violentos, ind_cid_n_violentos])


    # Imprime na tela:
    # Índice global dos anos de crimes violentos e não violentos
    indic_global([jan21, jan22, jan23])

    # Top 20 cidades com maior índice de crimes violentos
    print("\n"+"-"*51 + "\nTop 20 cidades com maior indice de crimes violentos\n" + "-"*51)
    relatorio_top(ind_cid_violentos, 20, "decrescente")

    # Top 15 cidades com o menor índice
    print("\n"+"-"*51 + "\nTop 15 cidades com menor índice de crimes violentos\n" + "-"*51)
    relatorio_top(ind_cid_violentos, 15, "crescente")

    # Top 50 cidades com os maiores índices de crimes não violentos
    print("\n" + "-"*51 + "\nTop 50 cidades com os maiores índices de crimes não violentos\n" + "-"*51)
    relatorio_top(ind_cid_n_violentos, 50, "decrescente")

    # Top 7 cidades com o menor índice de crimes não violentos
    print("\n" + "-"*51 + "\nTop 7 cidades com os menores índices de crimes não violentos\n" + "-"*51)
    relatorio_top(ind_cid_n_violentos, 7, "crescente")

    
    # Cria um arquivo json contendo o índice de crimes violentos 
    save_csv("indice_cidades_crimes_violentos.json", ind_cid_violentos)

    # Cria um arquivo json contendo o índice de crimes não violentos
    save_csv("indice_cidades_crimes_nao_violentos.json", ind_cid_n_violentos)


"""
Salva arquivos JSON
"""
def save_csv(path, dicionario):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(dicionario, f, indent=4)
    except OSError:
        print("Could not save the file!")



"""
Imprime na tela as cidades "tops" de acordo com o chamador sendo o
dicionario = dicionário que deseja ordenar e mostrar na tela;
num = numero que você deseja imprimir na tela;
seletor = se deseja na ordem crescente ou decresente.
"""
def relatorio_top(dicionario, num, seletor):
    
    # FUNCIONOU! MAS NÃO SEI COMO! PODE ME EXPLICAR ESSA LINHA DE CÓDIGO?
    if seletor == "decrescente":
        ordenado = sorted(dicionario.items(), key=lambda city: city[1],reverse=True)
    else:
        ordenado = sorted(dicionario.items(), key=lambda city: city[1])
    for index, city in enumerate(ordenado):
        # COMO O SOR BOTOU O ZERO NA ESQUERDA NOS NUMEROS DE 1-9????
        print(f"{index+1} - {city[0]}: {city[1]}")
        if index == num-1:
            print("-" * 51)
            break


"""
        Essa função consolida todas as informações dos dicionários jan21, jan22, jan23 
    em 2 dicionários, um que tem a pontuação da cidade em crime violentos e o outro
    com a pontuação da cidade em crimes não violentos. 
        Os 2 dicionários são consolidados da seguinte maneria:
    CHAVE = "NOME DA CIDADE"
    VALOR = "PONTUAÇÃO"
    Ex.:{"Porto Alegre": 125, "Canoas": 96, "Viamão": 67}
"""
def consolid_dict(months_list, dicts_list):

    violento = dicts_list[0]
    n_violento = dicts_list[1] 

    # Interagir entre a listas de meses
    for num, mes in enumerate(months_list):
        # Interagir entre o mês
        for city in mes:
            # Interagir entre os nomes das cidades
            for name in city:
                # Interagir entre os valores de cada cidade
                value_n_violento = 0
                value_violento = 0
                for i, valor in enumerate(city[name]):
                    # name = nome da cidade
                    # city[name] = ["LISTA DE VALORES"]
                    if i == 3 or i == 5 or i == 8 or i == 10:
                        value_n_violento += valor * VALORES[i]
                    else:
                        value_violento += valor * VALORES[i]

                # Caso seja a primeira base de dados (jan21) crie essa chave e adicione o valor, se não some na chave
                if num == 0:
                    violento[name] = value_violento
                    n_violento[name] = value_n_violento
                else:
                    violento[name] += value_violento
                    n_violento[name] += value_n_violento


"""
Essa função interage com a lista principal e calcula a soma de cada ano para
crimes violentos e crimes não violentos e depois disponibiliza na tela
"""
def indic_global(months_list):
    print("-" * 61)
    print("Indicadores globais por ano")
    print("-" * 61)
    
    violentos = [0, 0, 0]
    nao_violentos = [0, 0, 0]
    
    for i, mes in enumerate(months_list):
        for municipios in mes:
            for item in municipios:
                for index, valor in enumerate(municipios[item]):
                    if index == 3 or index == 5 or index == 8 or index == 10:
                        nao_violentos[i] += (valor * VALORES[index])
                    else:
                        violentos[i] += (valor * VALORES[index])

    print(f"""Crimes violentos
- 2021: {violentos[0]}
- 2022: {violentos[1]}
- 2023: {violentos[2]}""")
    print(f"""Crimes não violentos
- 2021: {nao_violentos[0]}
- 2022: {nao_violentos[1]}
- 2023: {nao_violentos[2]}""")
    print("-"*51)

                                

def open_csv(path, lista):
    try:
        with open(path, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f, delimiter=";")
            next(csv_reader)  # Ignorar a primeira linha (cabeçalho)
            for linha in csv_reader:
                valores = [int(valor.strip()) for valor in linha[1:]]  # Remove os espaços e converte para inteiros
                lista.append({linha[0]: valores})
    except:
        print(f"File {path} NOT FOUND!")

if __name__ == "__main__":
    # Inicizando constante de valores de acordo com o crime
    VALORES = [0, 10, 0, 3, 0, 3, 2, 3, 1, 2, 2, 5, 10, 10]

    main()
