    
from grafos import crear_listas_adyacencia_dirigido
from grafos2 import crear_matriz_adyacencia_dirigido

nodos = ["Depo", "ZA", "ZB", "ZC", "ZD", "C1", "C2", "C3", ]
aristas = [("Depo", "ZA"), ("Depo", "ZB"), ("ZA", "ZC"),("ZA", "ZD"), ("ZB", "ZD"), ("ZC", "C1"), ("ZD", "C2"), ("ZD", "C3")]


lista_ady = crear_listas_adyacencia_dirigido(nodos, aristas)
matriz_ady = crear_matriz_adyacencia_dirigido(nodos, aristas)
for fila in matriz_ady:
    print(fila)
print(lista_ady)

def destinos_directos(lista_ady, nodo):
    print(f"Desde {nodo} se puede llegar directamente a: {lista_ady[nodo]}")

for nodo in nodos:
    destinos_directos(lista_ady, nodo)