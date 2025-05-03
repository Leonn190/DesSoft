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
