import funcoes as F

DadosGuardados = []
contador = 0

cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

usadas = []
validas = ['sem_combinacao','quadra','full_house','sequencia_baixa','sequencia_alta','cinco_iguais',"1","2","3","4","5","6"]
while contador < 12:

    Rolados = F.rolar_dados(5 - len(DadosGuardados))
    RR = 0
    sair1 = False
    sair2 = False

    while True:
        print (f"Dados rolados: {Rolados}")
        print (f"Dados guardados: {DadosGuardados}")
        print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        while True:
            jogada = input()

            if jogada == "1":
                print ("Digite o índice do dado a ser guardado (0 a 4):")
                indice = input()
                Rolados, DadosGuardados = F.guardar_dado(Rolados,DadosGuardados,int(indice))
                break
            elif jogada == "2":
                print ("Digite o índice do dado a ser removido (0 a 4):")
                indice = input()
                Rolados, DadosGuardados = F.remover_dado(Rolados,DadosGuardados,int(indice))
                break
            elif jogada == "3":
                if RR < 2:
                    Rolados = F.rolar_dados(5 - len(DadosGuardados))
                    RR += 1
                else:
                    print ("Você já usou todas as rerrolagens.")
                break
            elif jogada == "4":
                F.imprime_cartela(cartela)
                break
            elif jogada == "0":
                print ("Digite a combinação desejada:")
                while True:
                    categoria = input()
                    if categoria in validas:
                        if categoria not in usadas:
                            cartela = F.faz_jogada(DadosGuardados + Rolados,categoria,cartela)
                            usadas.append(categoria)
                            DadosGuardados = []
                            contador += 1
                            sair2 = True
                            sair1 = True
                            break
                        else:
                            print ("Essa combinação já foi utilizada.")
                    else:
                        print ("Combinação inválida. Tente novamente.")
            else:
                print ("Opção inválida. Tente novamente.")
            
            if sair1 == True:
                break
        if sair2 == True:
            break

F.imprime_cartela(cartela)
total = 0
for chave,valor in cartela["regra_simples"].items():
    if valor != -1:
        total += valor

if total >= 63:
    total += 35

for chave,valor in cartela['regra_avancada'].items():
    if valor != -1:
        total += valor

print (f"pontução total: {total}")
