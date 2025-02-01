# ⚙️ Búsqueda en Profundidad (DFS) en un Grafo
#### 💻 Proyecto en Python para realizar búsqueda en profundidad en un grafo representado en JSON.
> Este proyecto implementa la búsqueda en profundidad (DFS - Depth First Search) en un grafo dirigido representado mediante una lista de adyacencia almacenada en un archivo JSON. La búsqueda permite encontrar el camino entre un nodo inicial y un nodo objetivo dentro del grafo.

#### 🌐 Visualización del Grafo
---
![](/pp.png)

#### 🚀 Características
>+ **Carga de Datos desde JSON:** 
>   + Se carga la información del grafo desde un archivo JSON.
>+ **Obtención de Hijos:** 
>   + Se extraen los nodos hijos de un nodo dado.
>+ **Búsqueda en Profundidad (DFS):** 
>   + Se implementa el algoritmo de búsqueda en profundidad para encontrar un camino desde un nodo inicial hasta un nodo objetivo.
>+ **Interfaz por Consola (REPL):** 
>   + Se puede interactuar con el sistema mediante comandos en la terminal.

#### 📚 Estructura del Proyecto
    E1-Profundidad/
    │── grafo.json        # Archivo con la representación del grafo
    │── repl_PP.py           # Implementación de la búsqueda DFS y la consola interactiva


#### 🛠️ Instalación y Uso
    Clonar el repositorio.
	Ejecutar el programa: "repl_PP.py"
	Ejemplo de uso:
	        1 - Para buscar un camino desde "A" hasta "A3A", en la consola ingresar: primero_prof(G, "A", "A3A")
		2 - Salida esperada: "['A', 'AA', 'AAA', 'A3A']"
		3 - Para salir de la consola, ingresar: "quit()"

#### 🔄 Funcionamiento del Código
##### Carga de datos
    def cargarDatos():
    import json
    R = []
    with open('grafo.json') as entrada:
        R = json.load(entrada)
    G.extend(R)
##### Obtención de Hijos
    def obtener_hijos(G,Raiz):
    return [a for r,a in G if r == Raiz]
##### Algoritmo DFS
    def primero_prof(G, Raiz, Bus):
    pila = [(Raiz, [Raiz])]
    while pila:
        (nodo, camino) = pila.pop()
        if nodo == Bus:
            return camino
        hijos = obtener_hijos(G, nodo)
        for hijo in hijos:
            pila.append((hijo, camino + [hijo]))
    return None
##### Consola Interactiva (REPL)
    def consola():
    while True:
        R = input("> ")
        if R == "quit()":
            break
        P = eval(R)
        if P:
            print(P)

#### 🎨 Mejoras Futuras
>- **Visualización del grafo:** 
>Implementar una librería para visualizar el grafo de manera gráfica.
>- **Optimización del DFS:** 
>Mejorar la eficiencia del algoritmo utilizando conjuntos para evitar visitar nodos repetidos.
---
###### 🌟 ¡Gracias por revisar este proyecto! 
###### Si tienes sugerencias o mejoras, no dudes en contribuir. 🦊
