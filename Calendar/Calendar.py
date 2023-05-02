"""
Este programa faz um calendário no terminal utilizando o input do usuário
Exemplo: 
Informe o numero de dias do mes: 27
VALOR INVALIDO! Informe o numero de dias do mes: 33
VALOR INVALIDO! Informe o numero de dias do mes: 31
Informe o dia da semana: 8
VALOR INVALIDO! Informe o dia da semana: -1
VALOR INVALIDO! Informe o dia da semana: 6
DOM SEG TER QUA QUI SEX SAB
                    01  02
03  04  05  06  07  08  09
10  11  12  13  14  15  16
17  18  19  20  21  22  23
24  25  26  27  28  29  30
31
"""
# Pegar o numero de dias do mês do usuário e verificar se é válido
dias_do_mes = int(input("Informe o numero de dias do mês: "))
# Criando flag dos dias do mês
dias_validos = False
while True: 
    for i in range(28,32):
        if dias_do_mes == i:
            dias_validos = True
    if dias_validos == False:
        dias_do_mes = int(input("VALOR INVÁLIDO! Informe o número de dias do mês: "))
        for i in range(28, 32):
            if dias_do_mes == i:
                print(" ")
    else:
        break        
# Usando listas:  
#while True:
#   if dias_do_mes not in [28, 29, 30, 31]:
#       dias_do_mes = int(input("VALOR INVÁLIDO! Informe o número de dias do mês: "))
#       if dias_do_mes in [28, 29, 30, 31]:
#           print()
#   else:
#       break
    
# Pegar o numero da semana na qual o mês começa e verificar se é válido
dia_da_semana = int(input("Informe o dia da semana: "))
while True: 
    for i in range(1,8):
        if dias_do_mes == i:
            dias_validos = True
    if dias_validos == False:
        dias_do_mes = int(input("VALOR INVÀLIDO! Informe o dia da semana: "))
    else:
        break 
# Usando listas:  
#while True:
#    if dia_da_semana not in [1, 2, 3, 4, 5, 6, 7]:
#        dia_da_semana = int(input("VALOR INVÀLIDO! Informe o dia da semana: "))
#    else:
#        break

print()
# Imprimir na tela os dias da semana
print("DOM SEG TER QUA QUI SEX SAB\n")
dia = 1
max_semana = dia_da_semana
# Imprimir os espaços em branco dependendo de onde o mês começa
for n in range(dia_da_semana-1):
    print("    ", end="")
# Imprimir os dias até que todos os dias do mes já estejam na tela
while dia <= dias_do_mes:
    if max_semana <= 7:
        if dia < 10:
            print(f"0{dia}", end="  ")
        else:
            print(f"{dia}", end="  ")
        max_semana += 1
        dia += 1
    else:
        print()
        max_semana = 1
print("\n")
