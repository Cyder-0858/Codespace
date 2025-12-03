# ===========================================================
#                    TDA: GRAPH EDGE
# ===========================================================
# Esta clase representa una arista (conexión) en un grafo dirigido.
# Una arista conecta un nodo origen con un nodo destino y tiene un peso
# asociado que representa el "costo" de atravesar esa conexión.

class GraphEdge:
    # Constructor de la arista
    # Parámetros:
    #   - source: nodo de origen de la arista
    #   - destination: nodo de destino de la arista
    #   - weight: peso o costo de la arista (distancia, tiempo, etc.)
    def __init__(self, source, destination, weight):
        self.source = source          # Referencia al nodo origen
        self.destination = destination # Referencia al nodo destino
        self.weight = weight          # Peso numérico de la arista


# ===========================================================
#                    TDA: GRAPH NODE
# ===========================================================
# Esta clase representa un nodo (vértice) en el grafo.
# Cada nodo tiene un nombre identificador, una lista de aristas salientes,
# y atributos auxiliares para el algoritmo de Dijkstra.

class GraphNode:
    # Constructor del nodo
    # Parámetro:
    #   - name: identificador único del nodo (puede ser string, número, etc.)
    def __init__(self, name):
        self.name = name              # Identificador del nodo
        self.edges = []               # Lista de aristas que SALEN de este nodo
        self.distance = float('inf')  # Distancia mínima desde el origen (inicialmente infinito)
        self.previous = None          # Nodo anterior en el camino más corto (para reconstruir la ruta)

    # Método para añadir una arista saliente desde este nodo
    # Parámetros:
    #   - destination: nodo destino de la arista
    #   - weight: peso de la arista
    def add_edge(self, destination, weight):
        # Crea una nueva arista y la añade a la lista de aristas del nodo
        self.edges.append(GraphEdge(self, destination, weight))

    # Método para reiniciar los valores de Dijkstra del nodo
    # Se usa antes de ejecutar el algoritmo para limpiar resultados anteriores
    def reset(self):
        self.distance = float('inf')  # Reinicia la distancia a infinito
        self.previous = None          # Elimina la referencia al nodo previo


# ===========================================================
#                      TDA: GRAPH
# ===========================================================
# Esta clase representa un grafo dirigido completo.
# Utiliza un diccionario para almacenar los nodos, donde la clave
# es el nombre del nodo y el valor es el objeto GraphNode.

class Graph:
    # Constructor del grafo
    # Inicializa un grafo vacío
    def __init__(self):
        self.nodes = {}  # Diccionario: nombre -> GraphNode

    # Método para añadir un nodo al grafo
    # Si el nodo ya existe, simplemente lo retorna sin duplicar
    # Parámetro:
    #   - name: nombre/identificador del nodo a añadir
    # Retorna: el objeto GraphNode (nuevo o existente)
    def add_node(self, name):
        if name not in self.nodes:           # Verifica si el nodo NO existe
            self.nodes[name] = GraphNode(name)  # Crea y almacena el nuevo nodo
        return self.nodes[name]              # Retorna el nodo (nuevo o existente)

    # Método para añadir una arista dirigida al grafo
    # Automáticamente crea los nodos si no existen
    # Parámetros:
    #   - source_name: nombre del nodo origen
    #   - destination_name: nombre del nodo destino
    #   - weight: peso de la arista
    def add_edge(self, source_name, destination_name, weight):
        source = self.add_node(source_name)        # Obtiene o crea el nodo origen
        destination = self.add_node(destination_name)  # Obtiene o crea el nodo destino
        source.add_edge(destination, weight)       # Añade la arista al nodo origen

    # Método para obtener un nodo por su nombre
    # Parámetro:
    #   - name: nombre del nodo a buscar
    # Retorna: el GraphNode si existe, None si no existe
    def get_node(self, name):
        return self.nodes.get(name)  # Usa .get() para retornar None si no existe

    # Método para reiniciar las distancias de todos los nodos
    # Necesario antes de ejecutar Dijkstra desde un nuevo origen
    def reset_distances(self):
        for node in self.nodes.values():  # Itera sobre todos los nodos
            node.reset()                   # Reinicia cada nodo


# ===========================================================
#                   TDA: AVL NODE
# ===========================================================
# Esta clase representa un nodo del árbol AVL.
# El árbol AVL se usa como cola de prioridad para Dijkstra.
# Cada nodo almacena una clave (prioridad/distancia) y un valor (nodo del grafo).

class AVLNode:
    # Constructor del nodo AVL
    # Parámetros:
    #   - key: clave de ordenamiento (en Dijkstra, es la distancia)
    #   - value: valor almacenado (en Dijkstra, es el GraphNode)
    def __init__(self, key, value):
        self.key = key        # Clave para ordenar (distancia en Dijkstra)
        self.value = value    # Valor asociado (nodo del grafo)
        self.height = 1       # Altura del nodo (hoja = 1), para balanceo
        self.left = None      # Hijo izquierdo (claves menores)
        self.right = None     # Hijo derecho (claves mayores o iguales)


# ===========================================================
#              TDA: AVL TREE (PRIORITY QUEUE)
# ===========================================================
# Árbol AVL auto-balanceado usado como cola de prioridad.
# Permite inserción y extracción del mínimo en O(log n).
# El balanceo automático garantiza que el árbol no se degenere.

class AVLTree:
    # Constructor del árbol AVL
    # Inicializa un árbol vacío
    def __init__(self):
        self.root = None  # Raíz del árbol (None = árbol vacío)

    # Método auxiliar para obtener la altura de un nodo
    # Retorna 0 si el nodo es None, o la altura almacenada
    def _height(self, node):
        return node.height if node else 0

    # Método para actualizar la altura de un nodo
    # La altura es 1 + el máximo de las alturas de sus hijos
    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # Método para calcular el factor de balance de un nodo
    # Factor = altura(izquierdo) - altura(derecho)
    # Si |factor| > 1, el árbol está desbalanceado
    def _balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    # Rotación simple a la derecha
    # Se usa cuando hay desbalance hacia la izquierda (factor > 1)
    # 
    #       y                x
    #      / \              / \
    #     x   C    ->      A   y
    #    / \                  / \
    #   A   B                B   C
    #
    def _rotate_right(self, y):
        x = y.left           # x es el hijo izquierdo de y
        y.left = x.right     # El subárbol derecho de x pasa a ser izquierdo de y
        x.right = y          # y se convierte en hijo derecho de x
        self._update_height(y)  # Actualiza altura de y primero (ahora es hijo)
        self._update_height(x)  # Actualiza altura de x (ahora es padre)
        return x             # x es la nueva raíz del subárbol

    # Rotación simple a la izquierda
    # Se usa cuando hay desbalance hacia la derecha (factor < -1)
    #
    #     x                  y
    #    / \                / \
    #   A   y      ->      x   C
    #      / \            / \
    #     B   C          A   B
    #
    def _rotate_left(self, x):
        y = x.right          # y es el hijo derecho de x
        x.right = y.left     # El subárbol izquierdo de y pasa a ser derecho de x
        y.left = x           # x se convierte en hijo izquierdo de y
        self._update_height(x)  # Actualiza altura de x primero (ahora es hijo)
        self._update_height(y)  # Actualiza altura de y (ahora es padre)
        return y             # y es la nueva raíz del subárbol

    # Método público para insertar un elemento
    # Parámetros:
    #   - key: clave de ordenamiento
    #   - value: valor a almacenar
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    # Método privado recursivo para insertar
    # Realiza inserción BST estándar y luego balancea
    def _insert(self, node, key, value):
        # Caso base: llegamos a una posición vacía, crear nuevo nodo
        if not node:
            return AVLNode(key, value)

        # Inserción BST: menor va a la izquierda, mayor/igual a la derecha
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        # Actualizar altura del nodo actual
        self._update_height(node)
        
        # Calcular factor de balance
        balance = self._balance(node)

        # Caso 1: Desbalance izquierda-izquierda (LL)
        # El nuevo nodo se insertó en el subárbol izquierdo del hijo izquierdo
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        
        # Caso 2: Desbalance derecha-derecha (RR)
        # El nuevo nodo se insertó en el subárbol derecho del hijo derecho
        if balance < -1 and key >= node.right.key:
            return self._rotate_left(node)
        
        # Caso 3: Desbalance izquierda-derecha (LR)
        # El nuevo nodo se insertó en el subárbol derecho del hijo izquierdo
        # Requiere doble rotación: primero izquierda, luego derecha
        if balance > 1 and key >= node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Caso 4: Desbalance derecha-izquierda (RL)
        # El nuevo nodo se insertó en el subárbol izquierdo del hijo derecho
        # Requiere doble rotación: primero derecha, luego izquierda
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        # Si no hay desbalance, retornar el nodo sin cambios
        return node

    # Método público para extraer el elemento con clave mínima
    # En Dijkstra, extrae el nodo con menor distancia
    # Retorna: tupla (key, value) o None si el árbol está vacío
    def extract_min(self):
        if not self.root:
            return None
        # Extraer el mínimo y actualizar la raíz
        self.root, min_node = self._extract_min(self.root)
        return min_node.key, min_node.value

    # Método privado recursivo para extraer el mínimo
    # El mínimo está siempre en el nodo más a la izquierda
    # Retorna: tupla (nuevo_subárbol, nodo_extraído)
    def _extract_min(self, node):
        # Caso base: este es el nodo mínimo (no tiene hijo izquierdo)
        if not node.left:
            return node.right, node  # Su hijo derecho (o None) lo reemplaza

        # Recursión: seguir buscando en el subárbol izquierdo
        node.left, min_node = self._extract_min(node.left)
        
        # Actualizar altura después de la extracción
        self._update_height(node)
        
        # Calcular factor de balance
        balance = self._balance(node)

        # Rebalancear si es necesario (similar a inserción)
        # Desbalance hacia la derecha
        if balance < -1:
            if self._balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
        # Desbalance hacia la izquierda
        elif balance > 1:
            if self._balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)

        return node, min_node

    # Método para verificar si el árbol está vacío
    # Retorna: True si está vacío, False si tiene elementos
    def is_empty(self):
        return self.root is None


# ===========================================================
#              TDA: DIJKSTRA ALGORITHM
# ===========================================================
# Implementación del algoritmo de Dijkstra para encontrar
# los caminos más cortos desde un nodo origen a todos los demás.
# 
# Complejidad: O((V + E) * log V) donde:
#   - V = número de vértices (nodos)
#   - E = número de aristas
#   - log V viene del uso del AVL como cola de prioridad

class Dijkstra:
    # Constructor del algoritmo
    # Parámetro:
    #   - graph: el grafo sobre el cual ejecutar Dijkstra
    def __init__(self, graph):
        self.graph = graph

    # Método principal que ejecuta el algoritmo de Dijkstra
    # Calcula las distancias mínimas desde el nodo origen a todos los demás
    # Parámetro:
    #   - start_name: nombre del nodo origen
    def run(self, start_name):
        # Reiniciar todas las distancias a infinito antes de comenzar
        self.graph.reset_distances()
        
        # Obtener el nodo de inicio
        start = self.graph.get_node(start_name)
        if not start:
            raise ValueError(f"Nodo '{start_name}' no existe")

        # La distancia del origen a sí mismo es 0
        start.distance = 0
        
        # Crear la cola de prioridad (AVL) e insertar el nodo inicial
        pq = AVLTree()
        pq.insert(0, start)  # Insertar con distancia 0

        # Procesar nodos mientras haya elementos en la cola
        while not pq.is_empty():
            # Extraer el nodo con menor distancia
            dist, node = pq.extract_min()
            
            # OPTIMIZACIÓN: Si la distancia extraída es mayor que la actual,
            # este es un registro obsoleto (ya procesamos este nodo con menor distancia)
            # Esto ocurre porque no podemos "actualizar" claves en el AVL,
            # así que insertamos duplicados y descartamos los obsoletos aquí
            if dist > node.distance:
                continue

            # Relajación: examinar todas las aristas salientes del nodo actual
            for edge in node.edges:
                neighbor = edge.destination  # Nodo vecino
                new_dist = node.distance + edge.weight  # Nueva distancia potencial

                # Si encontramos un camino más corto al vecino
                if new_dist < neighbor.distance:
                    neighbor.distance = new_dist  # Actualizar distancia mínima
                    neighbor.previous = node      # Recordar de dónde venimos
                    pq.insert(new_dist, neighbor)  # Añadir a la cola con nueva prioridad

    # Método para reconstruir el camino más corto hacia un destino
    # Debe llamarse DESPUÉS de ejecutar run()
    # Parámetro:
    #   - destination_name: nombre del nodo destino
    # Retorna: lista con los nombres de los nodos del camino, o lista vacía si no hay camino
    def get_path(self, destination_name):
        dest = self.graph.get_node(destination_name)
        
        # Si el nodo no existe o no es alcanzable (distancia infinita)
        if not dest or dest.distance == float('inf'):
            return []

        # Reconstruir el camino siguiendo los punteros "previous"
        # Esto construye el camino en orden inverso (de destino a origen)
        path = []
        current = dest
        while current:
            path.append(current.name)
            current = current.previous  # Ir al nodo anterior
        
        # Invertir para obtener el camino de origen a destino
        return path[::-1]

    # Método para obtener la distancia mínima hacia un destino
    # Debe llamarse DESPUÉS de ejecutar run()
    # Parámetro:
    #   - destination_name: nombre del nodo destino
    # Retorna: la distancia mínima, o infinito si no es alcanzable
    def get_distance(self, destination_name):
        node = self.graph.get_node(destination_name)
        return node.distance if node else float('inf')


# ===========================================================
#                    EJEMPLO DE USO
# ===========================================================
# Demostración del funcionamiento del algoritmo con un grafo de ejemplo
#
# Grafo de ejemplo (dirigido con pesos):
#
#          4
#     A -------> B
#     |          |
#   2 |          | 5
#     v    1     v
#     C -------> D -------> F
#     |          |    6     ^
#  10 |        2 |          | 3
#     v          v          |
#     E <------- + -------> E
#                    
# Las aristas son:
# A->B(4), A->C(2), C->B(1), B->D(5), C->D(8), C->E(10), D->E(2), D->F(6), E->F(3)

if __name__ == "__main__":
    # Crear un nuevo grafo vacío
    g = Graph()

    # Añadir las aristas (los nodos se crean automáticamente)
    g.add_edge("A", "B", 4)   # Arista de A a B con peso 4
    g.add_edge("A", "C", 2)   # Arista de A a C con peso 2
    g.add_edge("C", "B", 1)   # Arista de C a B con peso 1
    g.add_edge("B", "D", 5)   # Arista de B a D con peso 5
    g.add_edge("C", "D", 8)   # Arista de C a D con peso 8
    g.add_edge("C", "E", 10)  # Arista de C a E con peso 10
    g.add_edge("D", "E", 2)   # Arista de D a E con peso 2
    g.add_edge("D", "F", 6)   # Arista de D a F con peso 6
    g.add_edge("E", "F", 3)   # Arista de E a F con peso 3

    # Crear instancia del algoritmo de Dijkstra para este grafo
    dijkstra = Dijkstra(g)
    
    # Ejecutar Dijkstra desde el nodo "A"
    dijkstra.run("A")

    # Mostrar las distancias mínimas calculadas desde A a cada nodo
    print("DISTANCIAS MÍNIMAS DESDE A:")
    for name in g.nodes:
        print(f"{name}: {g.get_node(name).distance}")

    # Mostrar los caminos más cortos desde A a cada destino
    print("\nCAMINOS MÁS CORTOS:")
    for dest in ["B", "C", "D", "E", "F"]:
        path = dijkstra.get_path(dest)      # Obtener el camino
        dist = dijkstra.get_distance(dest)  # Obtener la distancia
        # Formatear y mostrar: "A → X: A → ... → X (distancia: N)"
        print(f"A → {dest}: {' → '.join(path)} (distancia: {dist})")
