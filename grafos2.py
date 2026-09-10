def crear_matriz_adyacencia(nodos, aristas):
    n = len(nodos)
    matriz = [[0] * n for _ in range(n)]
    for u, v in aristas:
        i = nodos.index(u)
        j = nodos.index(v)
        matriz[i][j] = 1
        matriz[j][i] = 1
    return matriz


def crear_matriz_adyacencia_dirigido(nodos, aristas):
    n = len(nodos)
    matriz = [[0] * n for _ in range(n)]
    for u, v in aristas:
        i = nodos.index(u)
        j = nodos.index(v)
        matriz[i][j] = 1
    return matriz


if __name__ == "__main__":
    nodos = [1, 2, 3, 4, 5]
    aristas = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]
    resultado = crear_matriz_adyacencia(nodos, aristas)
    print(resultado)