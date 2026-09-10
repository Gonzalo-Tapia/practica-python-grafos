def crear_listas_adyacencia(nodos, aristas):
    listas_adyacencia = {}
    for nodo in nodos:
        listas_adyacencia[nodo] = []
    for u, v in aristas:
        listas_adyacencia[u].append(v)
        listas_adyacencia[v].append(u)
    return listas_adyacencia


def grado_nodo(listas_adyacencia, nodo):
    return len(listas_adyacencia[nodo])


def son_adyacentes(listas_adyacencia, nodo1, nodo2):
    return nodo2 in listas_adyacencia[nodo1]


def crear_listas_adyacencia_dirigido(nodos, aristas):
    listas_adyacencia_dirigido = {}
    for nodo in nodos:
        listas_adyacencia_dirigido[nodo] = []
    for u, v in aristas:
        listas_adyacencia_dirigido[u].append(v)
    return listas_adyacencia_dirigido


def grado_entrada_salida(listas_adyacencia_dirigido, nodo):
    grado_salida = len(listas_adyacencia_dirigido[nodo])
    grado_entrada = 0
    for lista_vecinos in listas_adyacencia_dirigido.values():
        if nodo in lista_vecinos:
            grado_entrada += 1
    return (grado_entrada, grado_salida)


if __name__ == "__main__":
    # Pruebas del grafo no dirigido (Ejercicio 1)
    nodos = [1, 2, 3, 4, 5]
    aristas = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]
    listas = crear_listas_adyacencia(nodos, aristas)
    print(listas)

    for nodo in nodos:
        print(f"el nodo {nodo}, tiene grado {grado_nodo(listas, nodo)}")

    pares = [(1, 3), (1, 4), (4, 5)]
    for a, b in pares:
        print(f"¿{a} y {b} son adyacentes? {son_adyacentes(listas, a, b)}")

    # Pruebas del grafo dirigido (Ejercicio 2)
    nodos_dir = ['A', 'B', 'C', 'D']
    aristas_dir = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
    grafo_dirigido = crear_listas_adyacencia_dirigido(nodos_dir, aristas_dir)
    print(grafo_dirigido)

    for nodo in nodos_dir:
        print(f"Nodo {nodo}: {grado_entrada_salida(grafo_dirigido, nodo)}")