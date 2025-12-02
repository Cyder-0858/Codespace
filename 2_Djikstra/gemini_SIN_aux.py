class Arista:
    def __init__(self, destino, peso):
        # 'destino' es el OBJETO Vertice
        self.destino = destino  
        self.peso = peso

class Vertice:
    def __init__(self, dato):
        self.dato = dato
        self.vecinos = [] # Lista de objetos Arista

    def agregar_vecino(self, vertice_destino, peso):
        nueva_arista = Arista(vertice_destino, peso)
        self.vecinos.append(nueva_arista)

class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.vertices = {}

    def agregar_vertice(self, dato):
        if dato not in self.vertices:
            self.vertices[dato] = Vertice(dato)
            return True
        return False

    def agregar_arista(self, dato_origen, dato_destino, peso):
        if dato_origen in self.vertices and dato_destino in self.vertices:
            nodo_origen = self.vertices[dato_origen]
            nodo_destino = self.vertices[dato_destino]
            
            nodo_origen.agregar_vecino(nodo_destino, peso)
            
            if not self.dirigido:
                nodo_destino.agregar_vecino(nodo_origen, peso)
        else:
            print(f"Error: No se pueden unir '{dato_origen}' y '{dato_destino}'.")

    # --- ALGORITMO DIJKSTRA MANUAL ---
    def dijkstra(self, dato_inicio, dato_fin):
        # 1. Inicialización
        # distancias: Guardará la distancia más corta conocida desde inicio hasta cada nodo
        distancias = {dato: float('inf') for dato in self.vertices}
        distancias[dato_inicio] = 0
        
        # padres: Para reconstruir el camino al final
        padres = {dato: None for dato in self.vertices}
        
        # no_visitados: Lista de nodos que aún debemos evaluar
        no_visitados = list(self.vertices.keys())

        while no_visitados:
            # 2. SELECCIÓN MANUAL DEL NODO CON MENOR DISTANCIA
            # Como no usamos librerías, buscamos a mano en la lista 'no_visitados'
            nodo_actual = None
            distancia_minima_actual = float('inf')

            for nodo in no_visitados:
                if distancias[nodo] < distancia_minima_actual:
                    distancia_minima_actual = distancias[nodo]
                    nodo_actual = nodo

            # Si nodo_actual sigue siendo None o infinito, es que los nodos restantes
            # son inalcanzables o ya terminamos los caminos posibles.
            if nodo_actual is None:
                break

            # Si ya llegamos al destino, podemos detener el algoritmo para optimizar
            if nodo_actual == dato_fin:
                break

            # Marcamos como visitado sacándolo de la lista
            no_visitados.remove(nodo_actual)

            # 3. RELAJACIÓN DE ARISTAS (Verificar vecinos)
            objeto_vertice_actual = self.vertices[nodo_actual]
            
            for arista in objeto_vertice_actual.vecinos:
                dato_vecino = arista.destino.dato
                peso = arista.peso
                
                # Solo procesamos si el vecino no ha sido visitado aún (opcional, pero eficiente)
                if dato_vecino in no_visitados:
                    nueva_distancia = distancias[nodo_actual] + peso
                    
                    if nueva_distancia < distancias[dato_vecino]:
                        distancias[dato_vecino] = nueva_distancia
                        padres[dato_vecino] = nodo_actual

        # 4. RECONSTRUCCIÓN DEL CAMINO (Backtracking)
        camino = []
        nodo = dato_fin
        
        # Si la distancia es infinita, no hay camino
        if distancias[dato_fin] == float('inf'):
            return [], float('inf')

        while nodo is not None:
            camino.insert(0, nodo) # Insertar al principio
            nodo = padres[nodo]

        return camino, distancias[dato_fin]

# --- PRUEBA DEL CÓDIGO ---

g = Grafo(dirigido=False)

# Agregamos vértices
for v in ["A", "B", "C", "D", "E"]:
    g.agregar_vertice(v)

# Agregamos caminos (Aristas)
g.agregar_arista("A", "B", 4)
g.agregar_arista("A", "C", 2)
g.agregar_arista("C", "B", 1) 
g.agregar_arista("B", "D", 5)
g.agregar_arista("C", "D", 8)
g.agregar_arista("C", "E", 10)
g.agregar_arista("D", "E", 2) 

print("Calculando ruta de A hacia E...")
ruta, costo = g.dijkstra("A", "E")

if ruta:
    print(f"Ruta encontrada: {' -> '.join(ruta)}")
    print(f"Costo total: {costo}")
else:
    print("No existe ruta entre los nodos seleccionados.")