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


class EstadoDijkstra:
    """
    Clase auxiliar para guardar el estado de cada nodo
    DURANTE la ejecución del algoritmo.
    """
    def __init__(self, vertice):
        self.vertice = vertice
        self.distancia = float('inf') # Distancia tentativa
        self.padre = None             # Para reconstruir el camino
        self.visitado = False         # ¿Ya lo revisamos?

    # Opcional: Esto ayuda si quisieras ordenar una lista de objetos de este tipo
    def __lt__(self, otro):
        return self.distancia < otro.distancia

# --- DENTRO DE TU CLASE GRAFO ---
    def dijkstra_con_clase_auxiliar(self, dato_inicio, dato_fin):
        # 1. Crear el mapa de estados (Diccionario de dato -> Objeto Estado)
        # Esto reemplaza a tener distancias{}, padres{} y visitados[] por separado
        estados = {
            dato: EstadoDijkstra(v) 
            for dato, v in self.vertices.items()
        }

        # Configurar nodo inicial
        estados[dato_inicio].distancia = 0

        # Bucle principal
        while True:
            # A. SELECCIÓN: Buscar el nodo NO visitado con menor distancia
            nodo_actual_estado = None
            menor_distancia = float('inf')

            for estado in estados.values():
                if not estado.visitado and estado.distancia < menor_distancia:
                    menor_distancia = estado.distancia
                    nodo_actual_estado = estado

            # Si no encontramos nada o la distancia es inf, terminamos
            if nodo_actual_estado is None:
                break
            
            # Si llegamos al destino, paramos
            if nodo_actual_estado.vertice.dato == dato_fin:
                break

            # B. MARCAR COMO VISITADO
            nodo_actual_estado.visitado = True
            
            # C. RELAJACIÓN (Revisar vecinos)
            # Fíjate que accedemos al objeto Vertice original a través de .vertice
            for arista in nodo_actual_estado.vertice.vecinos:
                dato_vecino = arista.destino.dato
                peso = arista.peso
                estado_vecino = estados[dato_vecino]

                if not estado_vecino.visitado:
                    nueva_dist = nodo_actual_estado.distancia + peso
                    if nueva_dist < estado_vecino.distancia:
                        estado_vecino.distancia = nueva_dist
                        estado_vecino.padre = nodo_actual_estado.vertice.dato

        # 4. RECONSTRUCCIÓN (Igual que antes, pero leyendo del objeto estado)
        camino = []
        actual = dato_fin
        
        if estados[actual].distancia == float('inf'):
            return [], float('inf')

        while actual is not None:
            camino.insert(0, actual)
            actual = estados[actual].padre

        return camino, estados[dato_fin].distancia