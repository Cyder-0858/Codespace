# ===========================================================
#                    TDA: GRAPH EDGE
# ===========================================================

class GraphEdge:
    """
    TDA que representa una arista del grafo.
    Contiene origen, destino y peso.
    """
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.source.name} --{self.weight}--> {self.destination.name}"


# ===========================================================
#                    TDA: GRAPH NODE
# ===========================================================

class GraphNode:
    """
    TDA que representa un vértice del grafo.
    Contiene nombre, lista de aristas, distancia mínima y predecesor.
    """
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.distance = float('inf')
        self.previous = None

    def add_edge(self, destination, weight):
        """Agrega una arista desde este nodo hacia el destino."""
        edge = GraphEdge(self, destination, weight)
        self.edges.append(edge)

    def reset(self):
        """Reinicia la distancia y predecesor del nodo."""
        self.distance = float('inf')
        self.previous = None

    def __repr__(self):
        return f"GraphNode({self.name})"

    def __lt__(self, other):
        """Permite comparar nodos por nombre (útil para desempates)."""
        return self.name < other.name


# ===========================================================
#                      TDA: GRAPH
# ===========================================================

class Graph:
    """
    TDA que representa un grafo dirigido con pesos positivos.
    Permite agregar vértices y aristas, y resetear el estado.
    """
    def __init__(self):
        self.nodes = {}  # diccionario: nombre -> GraphNode

    def add_node(self, name):
        """Crea y devuelve un nuevo nodo si no existía."""
        if name not in self.nodes:
            self.nodes[name] = GraphNode(name)
        return self.nodes[name]

    def add_edge(self, source_name, destination_name, weight):
        """Crea una arista desde source hacia destination con el peso dado."""
        source = self.add_node(source_name)
        destination = self.add_node(destination_name)
        source.add_edge(destination, weight)

    def get_node(self, name):
        """Retorna el nodo con el nombre dado, o None si no existe."""
        return self.nodes.get(name)

    def reset_distances(self):
        """Reinicia las distancias y predecesores de todos los nodos."""
        for node in self.nodes.values():
            node.reset()

    def __repr__(self):
        return f"Graph(nodes={len(self.nodes)})"


# ===========================================================
#                   TDA: AVL NODE
# ===========================================================

class AVLNode:
    """
    TDA que representa un nodo del árbol AVL.
    Contiene clave (prioridad), valor, altura y referencias a hijos.
    """
    def __init__(self, key, value):
        self.key = key      # distancia (prioridad)
        self.value = value  # GraphNode asociado
        self.height = 1
        self.left = None
        self.right = None

    def __repr__(self):
        return f"AVLNode(key={self.key}, value={self.value.name})"


# ===========================================================
#              TDA: AVL TREE (PRIORITY QUEUE)
# ===========================================================

class AVLTree:
    """
    TDA Árbol AVL usado como cola de prioridad para Dijkstra.
    Mantiene las operaciones balanceadas con complejidad O(log n).
    """
    def __init__(self):
        self.root = None

    # -------------------- Utilidades --------------------

    def _get_height(self, node):
        """Retorna la altura del nodo, o 0 si es None."""
        return node.height if node else 0

    def _update_height(self, node):
        """Actualiza la altura del nodo basándose en sus hijos."""
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))

    def _get_balance_factor(self, node):
        """Calcula el factor de balance del nodo."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # -------------------- Rotaciones --------------------

    def _rotate_right(self, y):
        """Rotación simple a la derecha."""
        x = y.left
        T2 = x.right

        # Realizar rotación
        x.right = y
        y.left = T2

        # Actualizar alturas
        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        """Rotación simple a la izquierda."""
        y = x.right
        T2 = y.left

        # Realizar rotación
        y.left = x
        x.right = T2

        # Actualizar alturas
        self._update_height(x)
        self._update_height(y)

        return y

    # -------------------- Inserción --------------------

    def insert(self, key, value):
        """Inserta un nuevo elemento (key, value) en el AVL."""
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """Inserción recursiva con balanceo automático."""
        # Caso base: crear nuevo nodo
        if not node:
            return AVLNode(key, value)

        # Inserción recursiva
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        # Actualizar altura
        self._update_height(node)

        # Obtener factor de balance
        balance = self._get_balance_factor(node)

        # Caso 1: Izquierda-Izquierda
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Caso 2: Derecha-Derecha
        if balance < -1 and key >= node.right.key:
            return self._rotate_left(node)

        # Caso 3: Izquierda-Derecha
        if balance > 1 and key >= node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Caso 4: Derecha-Izquierda
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # -------------------- Extracción del Mínimo --------------------

    def extract_min(self):
        """
        Extrae y retorna el elemento con menor clave (prioridad).
        Retorna: (key, value) o None si el árbol está vacío.
        """
        if not self.root:
            return None
        
        self.root, min_node = self._extract_min(self.root)
        return min_node.key, min_node.value

    def _extract_min(self, node):
        """
        Extrae recursivamente el nodo mínimo y rebalancea.
        Retorna: (nuevo_subárbol, nodo_mínimo)
        """
        # El mínimo está en el extremo izquierdo
        if node.left is None:
            return node.right, node

        # Buscar mínimo recursivamente
        node.left, min_node = self._extract_min(node.left)

        # Actualizar altura
        self._update_height(node)

        # Rebalancear
        balance = self._get_balance_factor(node)

        # Caso 1: Desbalance derecha
        if balance < -1:
            right_balance = self._get_balance_factor(node.right)
            if right_balance <= 0:
                # Derecha-Derecha
                node = self._rotate_left(node)
            else:
                # Derecha-Izquierda
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)

        # Caso 2: Desbalance izquierda
        elif balance > 1:
            left_balance = self._get_balance_factor(node.left)
            if left_balance >= 0:
                # Izquierda-Izquierda
                node = self._rotate_right(node)
            else:
                # Izquierda-Derecha
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)

        return node, min_node

    def is_empty(self):
        """Verifica si el árbol está vacío."""
        return self.root is None

    def __repr__(self):
        return f"AVLTree(empty={self.is_empty()})"


# ===========================================================
#              TDA: DIJKSTRA ALGORITHM
# ===========================================================

class Dijkstra:
    """
    TDA que implementa el algoritmo de Dijkstra usando un AVL Tree
    como cola de prioridad para encontrar caminos más cortos.
    """
    def __init__(self, graph):
        self.graph = graph

    def run(self, start_name):
        """
        Ejecuta el algoritmo de Dijkstra desde el nodo inicial.
        Calcula las distancias mínimas a todos los nodos alcanzables.
        """
        # Reiniciar el grafo
        self.graph.reset_distances()

        # Obtener nodo inicial
        start_node = self.graph.get_node(start_name)
        if not start_node:
            raise ValueError(f"Nodo '{start_name}' no existe en el grafo")

        # Inicializar
        start_node.distance = 0
        priority_queue = AVLTree()
        priority_queue.insert(0, start_node)

        # Algoritmo principal
        while not priority_queue.is_empty():
            current_distance, current_node = priority_queue.extract_min()

            # Ignorar entradas obsoletas
            if current_distance > current_node.distance:
                continue

            # Relajación de aristas
            for edge in current_node.edges:
                neighbor = edge.destination
                new_distance = current_node.distance + edge.weight

                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    neighbor.previous = current_node
                    priority_queue.insert(new_distance, neighbor)

    def get_shortest_path(self, destination_name):
        """
        Reconstruye el camino más corto desde el origen hasta el destino.
        Retorna: lista de nombres de nodos en orden.
        """
        destination = self.graph.get_node(destination_name)
        if not destination:
            return []

        if destination.distance == float('inf'):
            return []  # No hay camino

        # Reconstruir camino
        path = []
        current = destination
        while current is not None:
            path.append(current.name)
            current = current.previous

        path.reverse()
        return path

    def get_distance(self, destination_name):
        """Retorna la distancia mínima al nodo destino."""
        node = self.graph.get_node(destination_name)
        return node.distance if node else float('inf')

    def get_all_distances(self):
        """Retorna un diccionario con todas las distancias calculadas."""
        return {name: node.distance for name, node in self.graph.nodes.items()}


# ===========================================================
#                    EJEMPLO DE USO
# ===========================================================

if __name__ == "__main__":
    # Crear grafo
    g = Graph()

    # Agregar aristas (automáticamente crea los nodos)
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("C", "B", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)
    g.add_edge("D", "F", 6)
    g.add_edge("E", "F", 3)

    # Crear instancia de Dijkstra
    dijkstra = Dijkstra(g)

    # Ejecutar desde nodo A
    dijkstra.run("A")

    # Mostrar resultados
    print("=" * 50)
    print("DISTANCIAS MÍNIMAS DESDE A:")
    print("=" * 50)
    for node_name, distance in dijkstra.get_all_distances().items():
        print(f"{node_name}: {distance}")

    print("\n" + "=" * 50)
    print("CAMINOS MÁS CORTOS:")
    print("=" * 50)
    
    for destination in ["B", "C", "D", "E", "F"]:
        path = dijkstra.get_shortest_path(destination)
        distance = dijkstra.get_distance(destination)
        print(f"A → {destination}: {' → '.join(path)} (distancia: {distance})")