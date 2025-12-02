# ===========================================================
#                      TDA: VÉRTICE
# ===========================================================

class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []
        # Usamos float('inf') que es nativo de Python, no requiere importar math
        self.distance = float('inf') 
        self.previous = None

    def add_edge(self, to, weight):
        self.edges.append(Edge(self, to, weight))

    def __repr__(self):
        return f"Vertex({self.name})"


# ===========================================================
#                       TDA: ARISTA
# ===========================================================

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return f"{self.src.name} --{self.weight}--> {self.dest.name}"


# ===========================================================
#                       TDA: GRAFO
# ===========================================================

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        v = Vertex(name)
        self.vertices[name] = v
        return v

    def add_edge(self, src, dest, weight):
        # Asumimos que los vértices ya existen
        if src in self.vertices and dest in self.vertices:
            self.vertices[src].add_edge(self.vertices[dest], weight)

    def get_vertex(self, name):
        return self.vertices.get(name)


# ===========================================================
#           DIJKSTRA (SIN IMPORTAR NINGUNA LIBRERÍA)
# ===========================================================

def dijkstra(graph, start_name):
    start = graph.get_vertex(start_name)
    if not start:
        return
        
    start.distance = 0

    # Usamos una lista normal como cola
    # Estructura: Tupla (distancia, vertice_objeto)
    queue = [(0, start)]

    while len(queue) > 0:
        # SIMULACIÓN DE COLA DE PRIORIDAD SIN LIBRERÍAS:
        # Ordenamos la lista basada en la distancia (el primer elemento de la tupla)
        # para que el menor quede al principio.
        queue.sort(key=lambda x: x[0])

        # Extraemos el elemento con menor distancia
        current_dist, u = queue.pop(0)

        # Si encontramos una distancia mayor a la ya registrada, saltamos
        if current_dist > u.distance:
            continue

        # Revisar vecinos
        for edge in u.edges:
            v = edge.dest
            new_dist = u.distance + edge.weight

            if new_dist < v.distance:
                v.distance = new_dist
                v.previous = u
                # Agregamos a la cola para procesar
                queue.append((new_dist, v))


# ===========================================================
#            RECONSTRUCCIÓN DEL CAMINO ÓPTIMO
# ===========================================================

def reconstruct_path(graph, start, end):
    path = []
    current = graph.get_vertex(end)

    if not current or current.distance == float('inf'):
        return [] # No hay camino

    while current is not None:
        path.append(current.name)
        current = current.previous

    # Invertimos la lista manualmente usando slicing [::-1]
    return path[::-1]


# ===========================================================
#                       PRUEBA FINAL
# ===========================================================

# 1. Crear el grafo
g = Graph()

# Añadir vértices
nodos = ["A", "B", "C", "D", "E", "F"]
for name in nodos:
    g.add_vertex(name)

# Añadir aristas (Origen, Destino, Peso)
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "C", 1)
g.add_edge("B", "D", 5)
g.add_edge("C", "D", 8)
g.add_edge("C", "E", 10)
g.add_edge("D", "E", 2)
g.add_edge("D", "F", 6)
g.add_edge("E", "F", 3)

start_node = "A"
end_node = "F"

print(f"Calculando ruta mínima de {start_node} a {end_node}...")

# 2. Ejecutar Dijkstra
dijkstra(g, start_node)

# 3. Reconstruir camino
camino = reconstruct_path(g, start_node, end_node)

# 4. Mostrar Resultados en consola
print("\n" + "="*30)
print("       DISTANCIAS MÍNIMAS")
print("="*30)
for nombre in nodos:
    v = g.get_vertex(nombre)
    dist_str = v.distance if v.distance != float('inf') else "Infinito"
    print(f"Nodo {v.name}: {dist_str}")

print("\n" + "="*30)
print(f"    CAMINO ÓPTIMO A '{end_node}'")
print("="*30)

if camino:
    # Unir lista con flechas
    ruta_visual = " -> ".join(camino)
    print(ruta_visual)
    print(f"\nCosto total del viaje: {g.get_vertex(end_node).distance}")
else:
    print("No existe un camino posible entre los nodos seleccionados.")