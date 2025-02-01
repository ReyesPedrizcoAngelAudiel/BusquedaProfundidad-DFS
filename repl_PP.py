#Cargar la informacion
G = []
#Generar una funcion para obtener los hijos del grafo
#Si me dan el Grafo de la Raiz "A", obtendre 
def obtener_hijos(G,Raiz):
    #EL grafo esta representado como una lista de listas
    return [a for r,a in G if r == Raiz]

def cargarDatos():
    import json
    R = []
    with open('grafo.json') as entrada:
        R = json.load(entrada)
    G.extend(R)

#G    - grafo
#Raiz - Raiz o nodo inicial
#Bus  - El nodo a buscar
#El de profundidad (DFS) va de los hijos hasta el nodo raiz hasta encontrar el que el usuario necesita
def primero_prof(G, Raiz, Bus):
    # Pila para llevar el rastro del camino actual (nodos visitados) | Cada elemento es una tupla (nodo actual, camino)
    pila = [(Raiz, [Raiz])]
    
    while pila:                                             # Mientras haya elementos en la pila
        (nodo, camino) = pila.pop()                         # Extraer el nodo actual y el camino seguido hasta él
        if nodo == Bus:                                     # Si el nodo actual es el que buscamos, retornar el camino
            return camino
        hijos = obtener_hijos(G, nodo)                      # Obtener los hijos del nodo actual
        for hijo in hijos:                                  # Agregar cada hijo a la pila, extendiendo el camino actual
            pila.append((hijo, camino + [hijo]))
    return None                                             # Si no se encuentra el nodo buscado, retornar None

#Consola
def consola():
    #Read Evualte Print Loop (REPL)
    #Ciclo infinito:
    Terminar = False
    while not Terminar:
        #Leer
        R = input(">")
        #Si la lectura es un "quit()" | Termina el ciclo
        if R == "quit()":
            Terminar = True
            continue
        #Evaluate
        P = eval(R)
        #Solo aparecer cuando haya un valor, eliminando los NONE al cargar las funciones
        if P:
            #Imprimir
            print(P)

if __name__ == "__main__":
    cargarDatos()
    consola()