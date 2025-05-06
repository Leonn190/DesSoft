import random

def rolar_dados(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(1,6))
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    del dados_rolados[dado_para_guardar]
    return [dados_rolados,dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    pontos = {i: 0 for i in range(1, 7)}
    for d in dados:
        if 1 <= d <= 6:
            pontos[d] += d
    return pontos

def calcula_pontos_soma(dados):
    total = 0
    for d in dados:
        total += d
    return total

def calcula_pontos_sequencia_baixa(dados):
    conjunto = set(dados)
    sequencias_validas = [
        {1, 2, 3, 4},
        {2, 3, 4, 5},
        {3, 4, 5, 6}
    ]
    for seq in sequencias_validas:
        if seq.issubset(conjunto):
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    conjunto = set(dados)
    sequencias_validas = [
        {1, 2, 3, 4, 5},
        {2, 3, 4, 5, 6},
    ]
    for seq in sequencias_validas:
        if seq.issubset(conjunto):
            return 30
    return 0

def calcula_pontos_full_house(dados):
    contagem = {}
    for d in dados:
        if d in contagem:
            contagem[d] += 1
        else:
            contagem[d] = 1

    valores = list(contagem.values())
    if sorted(valores) == [2, 3]:
        total = 0
        for d in dados:
            total += d
        return total
    else:
        return 0

def calcula_pontos_quadra(dados):
    contagem = {}
    for d in dados:
        if d in contagem:
            contagem[d] += 1
        else:
            contagem[d] = 1

    for quantidade in contagem.values():
        if quantidade >= 4:
            total = 0
            for d in dados:
                total += d
            return total
    return 0

def calcula_pontos_quina(dados):
    contagem = {}
    for d in dados:
        if d in contagem:
            contagem[d] += 1
        else:
            contagem[d] = 1

    for quantidade in contagem.values():
        if quantidade >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    # Dicionário com as pontuações de todas as regras avançadas
    pontos = {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }
    return pontos

def faz_jogada(dados, categoria, cartela_de_pontos):
    try:
        num = int(categoria)
        if cartela_de_pontos['regra_simples'][num] == -1:
            pontos_simples = calcula_pontos_regra_simples(dados)
            cartela_de_pontos['regra_simples'][num] = pontos_simples[num]
    except ValueError:
        if categoria in cartela_de_pontos['regra_avancada']:
            if cartela_de_pontos['regra_avancada'][categoria] == -1:
                pontos_avancados = calcula_pontos_regra_avancada(dados)
                cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
