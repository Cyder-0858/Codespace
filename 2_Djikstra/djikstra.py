# ====================================================================================
# TDA: Vertex
# ====================================================================================
class Vertex:
    """
    TDA que representa un vértice del grafo.
    Contiene su nombre, lista de aristas, distancia y previo (para reconstrucción).
    """
    def __init__(self, name):
        self.name = name
        self.edges = []              # Lista de Edge
        self.distance = float('inf') # Distancia mínima conocida
        self.previous = None         # Para reconstrucción del camino

    def add_edge(self, dest, weight):
        self.edges.append(Edge(self, dest, weight))

    def __lt__(self, other):
        """Permite que los vértices puedan ser comparados en el heap si hay empates."""
        return self.name < other.name

    def __repr__(self):
        return f"Vertex({self.name})"


# ====================================================================================
# TDA: Edge
# ====================================================================================
class Edge:
    """
    TDA que representa una arista: origen, destino y peso.
    """
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


# ====================================================================================
# TDA: Graph
# ====================================================================================
class Graph:
    """
    TDA que representa un grafo dirigido con pesos positivos.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)
        return self.vertices[name]

    def add_edge(self, src, dest, weight):
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        self.vertices[src].add_edge(self.vertices[dest], weight)

    def get_vertex(self, name):
        return self.vertices.get(name)


# ====================================================================================
# TDA: MinHeap (implementación desde cero)
# ====================================================================================
class MinHeap:
    """
    TDA: Montículo binario mínimo (sin librerías externas).
    Maneja tuplas del tipo (distancia, vértice).
    """
    def __init__(self):
        self._heap = []

    def is_empty(self):
        return len(self._heap) == 0

    def push(self, item):
        self._heap.append(item)
        self._float_up(len(self._heap) - 1)

    def pop(self):
        if self.is_empty():
            return None
        min_val = self._heap[0]
        last = self._heap.pop()
        if not self.is_empty():
            self._heap[0] = last
            self._sink_down(0)
        return min_val

    def _float_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self._heap[index][0] < self._heap[parent][0]:
            self._swap(index, parent)
            self._float_up(parent)

    def _sink_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self._heap)

        if left < size and self._heap[left][0] < self._heap[smallest][0]:
            smallest = left
        if right < size and self._heap[right][0] < self._heap[smallest][0]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._sink_down(smallest)

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]


# ====================================================================================
# Dijkstra Solver (TDA independiente del grafo)
# ====================================================================================
class Dijkstra:
    """
    TDA que implementa el algoritmo de Dijkstra usando un MinHeap propio.
    """
    def __init__(self, graph):
        self.graph = graph

    def run(self, start_name):
        start = self.graph.get_vertex(start_name)
        if not start:
            return

        # Inicializar distancias
        for v in self.graph.vertices.values():
            v.distance = float('inf')
            v.previous = None

        start.distance = 0

        heap = MinHeap()
        heap.push((0, start))

        while not heap.is_empty():
            dist_u, u = heap.pop()

            if dist_u > u.distance:
                # Entrada obsoleta
                continue

            for edge in u.edges:
                v = edge.dest
                new_dist = u.distance + edge.weight

                if new_dist < v.distance:
                    v.distance = new_dist
                    v.previous = u
                    heap.push((new_dist, v))

    def get_path(self, end_name):
        """
        Reconstruye el camino desde el origen hasta end_name.
        """
        end = self.graph.get_vertex(end_name)
        if not end:
            return []

        path = []
        current = end
        while current:
            path.append(current)
            current = current.previous
        path.reverse()
        return path


# ====================================================================================
# EJEMPLO DE USO
# ====================================================================================
if __name__ == "__main__":
    g = Graph()

    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("C", "B", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)

    d = Dijkstra(g)
    d.run("A")

    path = d.get_path("E")

    print("Camino más corto desde A hasta E:")
    print(" -> ".join(v.name for v in path))
    print("Distancia total:", g.get_vertex("E").distance)