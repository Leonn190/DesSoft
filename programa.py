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

while contador < 12:

    Rolados = F.rolar_dados(5 - len(DadosGuardados))

    while True:
        print (f"Dados rolados: {Rolados}")
        print (f"Dados guardados: {DadosGuardados}")
        print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        jogada = input()

        if jogada == "1":
            print ("Digite o índice do dado a ser guardado (0 a 4):")
            indice = input()
            Rolados, DadosGuardados = F.guardar_dado(Rolados,DadosGuardados,int(indice))
        if jogada == "2":
            print ("Digite o índice do dado a ser removido (0 a 4):")
            indice = input()
            Rolados, DadosGuardados = F.remover_dado(Rolados,DadosGuardados,int(indice))
        if jogada == "3":
            Rolados = F.rolar_dados(5 - len(DadosGuardados))
        if jogada == "4":
            F.imprime_cartela(cartela)
        if jogada == "0":
            print ("Digite a combinação desejada:")
            categoria = input()
            F.faz_jogada(DadosGuardados,categoria,cartela)
            DadosGuardados = []
            contador += 1
            break

F.imprime_cartela(cartela)
total = 0
for chave,valor in cartela["regra_simples"].items():
    if valor != -1:
        total += valor
for chave,valor in cartela['regra_avancada'].items():
    if valor != -1:
        total += valor

print (f"pontução total: {total}")
