class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.distance = float('inf')  # Infinito nativo
        self.previous = None

    def add_edge(self, to, weight):
        self.edges.append(Edge(self, to, weight))

    # --- AGREGADO IMPORTANTE ---
    # Esto permite comparar vértices directamente: v1 < v2
    # El Heap necesita esto si hay empate en las distancias.
    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"Vertex({self.name})"

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        if name not in self.vertices:
            v = Vertex(name)
            self.vertices[name] = v
            return v
        return self.vertices[name]

    def add_edge(self, src, dest, weight):
        if src in self.vertices and dest in self.vertices:
            self.vertices[src].add_edge(self.vertices[dest], weight)
            # Descomenta la siguiente linea si quieres grafo NO dirigido:
            # self.vertices[dest].add_edge(self.vertices[src], weight)

    def get_vertex(self, name):
        return self.vertices.get(name)
    
#--------------------------------------------------------------------------

    class MinHeap:
    def __init__(self):
        # Usamos una lista simple para representar el árbol
        # Hijos de i: 2*i + 1 (izq), 2*i + 2 (der)
        # Padre de i: (i - 1) // 2
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def push(self, item):
        """Agrega un elemento y lo sube hasta su posición correcta."""
        self.heap.append(item)
        self._float_up(len(self.heap) - 1)

    def pop(self):
        """Extrae el elemento más pequeño (la raíz)."""
        if self.is_empty():
            return None
        
        # 1. Guardamos el mínimo (la raíz actual)
        min_val = self.heap[0]
        
        # 2. Tomamos el último elemento de la lista
        last_item = self.heap.pop()
        
        # 3. Si aún quedan elementos, ponemos el último en la raíz y reordenamos
        if not self.is_empty():
            self.heap[0] = last_item
            self._sink_down(0)
            
        return min_val

    # --- MÉTODOS PRIVADOS DE ORDENAMIENTO ---

    def _float_up(self, index):
        """Burbujeo hacia arriba (si el hijo es menor que el padre)."""
        parent_index = (index - 1) // 2
        
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Intercambiar (Swap)
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Recursividad hacia arriba
            self._float_up(parent_index)

    def _sink_down(self, index):
        """Hundir elemento (si el padre es mayor que alguno de sus hijos)."""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        size = len(self.heap)

        # Verificamos hijo izquierdo
        if left_child < size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # Verificamos hijo derecho
        if right_child < size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # Si el más pequeño no es el actual, intercambiamos y seguimos bajando
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sink_down(smallest)