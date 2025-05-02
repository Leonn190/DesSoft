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