from outros.operacoes_problema import *

def busca_profundidade(grafo: MultiDiGraph):
    nodo = grafo.graph["estado_inicial"]      # seto o nodo inicial como o estado inicial
    inserir_nodo_grafo(grafo, 1, None, nodo)  # adiciona o nodo inicial no grafo

    if teste_objetivo(nodo):            # testo se esse estado é o final (teste objetivo)
        return solucao(grafo, nodo)     # se verdadeiro, retorno o caminho (solucao)

    borda = [nodo]   # borda eh uma PILHA de nodos a serem explorados
    explorado = []   # explorado eh uma lista de nodos já explorados
    chave = 2        # id para adicionar novos nodos no grafo
    while True:
        if not borda:   # se borda vazia, retorno lista vazia
            return []

        nodo = borda.pop(0)     # removo o elemento da borda
        explorado.append(nodo)  # e adiciono em explorado

        nodos_filhos, chave = acoes(grafo, chave, nodo)  # gero todas as acoes possiveis para esse nodo

        for nodo_novo in nodos_filhos:   # para cada um dos novos nodos
            if nao_borda_e_nao_explorado(nodo_novo, borda, explorado):   # se nao estiver em borda e nem em explorado

                if teste_objetivo(nodo_novo):           # testo se esse estado é o final (teste objetivo)
                    return solucao(grafo, nodo_novo)    # se verdadeiro, retorno o caminho (solucao)

                borda.insert(0, nodo_novo)              # se falso, adiciono o nodo na borda para ser explorado futuramente