import heapq

# -------------------------------------------------------
# Algoritmo de Montículos (Heap Algorithm)
# -------------------------------------------------------


class HeapAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def run(self):
        if not self.graph.start:
            print("El grafo no tiene nodo de inicio definido.")
            return

        # 1. Inicialización del Montículo (Priority Queue)
        pq = []
        
        # Insertar nodo inicial
        # heapq gestiona la lista 'pq' manteniendo siempre el menor elemento accesible
        heapq.heappush(pq, self.graph.start)
        
        visited = set()
        path_log = []

        print(f"--- Iniciando Procesamiento del Montículo desde: {self.graph.start.name} ---\n")

        # 2. Bucle Principal (Mientras haya nodos en el montículo)
        while pq:
            # EXTRAER: Saca el nodo con MENOR 'value' (prioridad)
            current = heapq.heappop(pq)

            # Evitar ciclos o reprocesar nodos cerrados
            if current.name in visited:
                continue
            visited.add(current.name)

            path_log.append(current)
            print(f"-> Extrayendo del Heap: {current} (Procesado)")

            # 3. EXPANDIR: Añadir vecinos al montículo
            for edge in current.edges:
                neighbor = edge.next_node
                
                if neighbor.name not in visited:
                    # (Opcional) Aquí podrías actualizar el valor del vecino acumulando costos
                    # neighbor.value = current.value + edge.cost 
                    
                    neighbor.parent = current
                    heapq.heappush(pq, neighbor)
                    print(f"   + Agregando vecino al Heap: {neighbor}")

        return path_log

