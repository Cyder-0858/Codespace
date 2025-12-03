# ===========================================================
#                    TDA: GRAPH EDGE (ARISTA)
# ===========================================================
# Una arista representa una CONEXIÓN entre dos nodos del grafo.
# Es como una carretera que conecta dos ciudades.
# Cada arista tiene:
#   - Un origen (de dónde sale)
#   - Un destino (a dónde llega)
#   - Un peso (el "costo" de recorrerla, puede ser distancia, tiempo, etc.)
# ===========================================================

class GraphEdge:
    def __init__(self, source, destination, weight):
        """
        Constructor de la arista.
        
        Parámetros:
        -----------
        source : GraphNode
            El nodo desde donde SALE la arista (origen)
        destination : GraphNode
            El nodo hacia donde LLEGA la arista (destino)
        weight : int/float
            El peso o costo de recorrer esta arista
            (puede representar distancia, tiempo, costo monetario, etc.)
        """
        self.source = source            # Guardamos referencia al nodo origen
        self.destination = destination  # Guardamos referencia al nodo destino
        self.weight = weight            # Guardamos el peso/costo de la arista


# ===========================================================
#                    TDA: GRAPH NODE (NODO)
# ===========================================================
# Un nodo representa un PUNTO o VÉRTICE en el grafo.
# Es como una ciudad en un mapa de carreteras.
# Cada nodo tiene:
#   - Un nombre (identificador único)
#   - Una lista de aristas que SALEN de él
#   - Atributos para Dijkstra: distancia calculada y nodo previo
# ===========================================================

class GraphNode:
    def __init__(self, name):
        """
        Constructor del nodo.
        
        Parámetros:
        -----------
        name : str
            Identificador único del nodo (ej: "A", "B", "Madrid", etc.)
        """
        self.name = name                  # Nombre/identificador del nodo
        self.edges = []                   # Lista de aristas que SALEN de este nodo
                                          # (las conexiones hacia otros nodos)
        
        # ---------- ATRIBUTOS PARA DIJKSTRA ----------
        # Estos valores se usan durante la ejecución del algoritmo
        
        self.distance = float('inf')      # Distancia acumulada desde el origen
                                          # Inicialmente es INFINITO porque no
                                          # sabemos cómo llegar a este nodo
        
        self.previous = None              # Referencia al nodo ANTERIOR en el camino
                                          # más corto. Se usa para reconstruir la ruta
                                          # al final del algoritmo

    def add_edge(self, destination, weight):
        """
        Añade una arista (conexión) desde este nodo hacia otro.
        
        Parámetros:
        -----------
        destination : GraphNode
            El nodo destino de la conexión
        weight : int/float
            El peso/costo de esta conexión
        
        Ejemplo:
        --------
        Si este nodo es "A" y hacemos add_edge(nodo_B, 5),
        creamos la conexión: A ---(5)---> B
        """
        # Creamos una nueva arista y la añadimos a nuestra lista
        # self = nodo origen (este nodo)
        # destination = nodo destino
        # weight = peso de la arista
        nueva_arista = GraphEdge(self, destination, weight)
        self.edges.append(nueva_arista)

    def reset(self):
        """
        Reinicia los valores de Dijkstra para este nodo.
        
        ¿Por qué es necesario?
        ----------------------
        Si ejecutamos Dijkstra desde el nodo A, todos los nodos
        tendrán distancias calculadas respecto a A.
        
        Si luego queremos ejecutar Dijkstra desde B, necesitamos
        "limpiar" esos valores para empezar de cero.
        
        Es como borrar el pizarrón antes de resolver otro problema.
        """
        self.distance = float('inf')  # Volvemos a "no sé cómo llegar"
        self.previous = None          # Volvemos a "no sé de dónde vengo"


# ===========================================================
#                      TDA: GRAPH (GRAFO)
# ===========================================================
# El grafo es la estructura COMPLETA que contiene todos los
# nodos y sus conexiones.
# Es como el mapa completo con todas las ciudades y carreteras.
# 
# Usamos un diccionario para almacenar los nodos:
#   - Clave: nombre del nodo (string)
#   - Valor: objeto GraphNode
# ===========================================================

class Graph:
    def __init__(self):
        """
        Constructor del grafo.
        Inicializa un diccionario vacío para almacenar los nodos.
        """
        self.nodes = {}  # Diccionario: {"nombre": GraphNode}
                         # Ejemplo: {"A": <GraphNode A>, "B": <GraphNode B>}

    def add_node(self, name):
        """
        Añade un nuevo nodo al grafo (si no existe).
        
        Parámetros:
        -----------
        name : str
            Nombre/identificador del nodo a crear
        
        Retorna:
        --------
        GraphNode : El nodo creado (o el existente si ya estaba)
        
        Nota:
        -----
        Si el nodo ya existe, simplemente lo devuelve sin crear duplicados.
        Esto es útil porque add_edge() llama a add_node() automáticamente.
        """
        # Solo creamos el nodo si NO existe en el diccionario
        if name not in self.nodes:
            self.nodes[name] = GraphNode(name)
        
        # Devolvemos el nodo (nuevo o existente)
        return self.nodes[name]

    def add_edge(self, source_name, destination_name, weight):
        """
        Añade una arista (conexión dirigida) entre dos nodos.
        
        Parámetros:
        -----------
        source_name : str
            Nombre del nodo ORIGEN
        destination_name : str
            Nombre del nodo DESTINO
        weight : int/float
            Peso/costo de la conexión
        
        Nota:
        -----
        - Si los nodos no existen, los crea automáticamente
        - La arista es DIRIGIDA: va de source → destination
        - Para grafo no dirigido, llamar dos veces con origen/destino invertidos
        
        Ejemplo:
        --------
        graph.add_edge("A", "B", 4)  # Crea: A ---(4)---> B
        """
        # Obtenemos (o creamos) los nodos origen y destino
        source = self.add_node(source_name)
        destination = self.add_node(destination_name)
        
        # Añadimos la arista desde el origen hacia el destino
        source.add_edge(destination, weight)

    def get_node(self, name):
        """
        Busca y devuelve un nodo por su nombre.
        
        Parámetros:
        -----------
        name : str
            Nombre del nodo a buscar
        
        Retorna:
        --------
        GraphNode : El nodo encontrado
        None : Si el nodo no existe
        """
        # .get() devuelve None si la clave no existe (en lugar de error)
        return self.nodes.get(name)

    def reset_distances(self):
        """
        Reinicia los valores de Dijkstra en TODOS los nodos.
        
        Se llama al inicio de cada ejecución de Dijkstra para
        asegurar que empezamos con valores "limpios".
        """
        # Iteramos sobre todos los nodos del grafo
        for node in self.nodes.values():
            node.reset()  # Cada nodo resetea su distance y previous


# ===========================================================
#                   TDA: AVL NODE (NODO AVL)
# ===========================================================
# Un nodo del árbol AVL almacena un par (clave, valor):
#   - clave (key): usado para ordenar (en Dijkstra, es la distancia)
#   - valor (value): el dato asociado (en Dijkstra, es el GraphNode)
# 
# También mantiene información para el balanceo:
#   - altura del subárbol
#   - referencias a hijos izquierdo y derecho
# ===========================================================

class AVLNode:
    def __init__(self, key, value):
        """
        Constructor del nodo AVL.
        
        Parámetros:
        -----------
        key : comparable (int, float, etc.)
            La clave de ordenación (en Dijkstra = distancia)
        value : any
            El valor asociado (en Dijkstra = GraphNode)
        """
        self.key = key        # Clave para ordenar (distancia en Dijkstra)
        self.value = value    # Valor almacenado (nodo del grafo en Dijkstra)
        self.height = 1       # Altura del subárbol (hojas tienen altura 1)
        self.left = None      # Hijo izquierdo (claves menores)
        self.right = None     # Hijo derecho (claves mayores o iguales)


# ===========================================================
#              TDA: AVL TREE (ÁRBOL AVL)
# ===========================================================
# El árbol AVL es un árbol binario de búsqueda AUTO-BALANCEADO.
# 
# ¿Por qué usarlo como cola de prioridad?
# - Inserción: O(log n)
# - Extraer mínimo: O(log n)
# - Siempre balanceado = rendimiento garantizado
# 
# En Dijkstra, necesitamos siempre procesar el nodo con MENOR
# distancia, por eso usamos una cola de prioridad.
# ===========================================================

class AVLTree:
    def __init__(self):
        """
        Constructor del árbol AVL.
        Inicializa un árbol vacío (sin raíz).
        """
        self.root = None  # Referencia a la raíz del árbol

    # ==================== MÉTODOS AUXILIARES ====================

    def _height(self, node):
        """
        Obtiene la altura de un nodo.
        
        Parámetros:
        -----------
        node : AVLNode o None
            El nodo del cual queremos la altura
        
        Retorna:
        --------
        int : La altura del nodo (0 si es None)
        
        Nota:
        -----
        - Un nodo None tiene altura 0
        - Una hoja (sin hijos) tiene altura 1
        - Un nodo interno tiene altura = 1 + max(altura_hijos)
        """
        return node.height if node else 0

    def _update_height(self, node):
        """
        Recalcula la altura de un nodo basándose en sus hijos.
        
        Parámetros:
        -----------
        node : AVLNode
            El nodo cuya altura queremos actualizar
        
        Fórmula:
        --------
        altura = 1 + max(altura_izquierda, altura_derecha)
        """
        altura_izq = self._height(node.left)
        altura_der = self._height(node.right)
        node.height = 1 + max(altura_izq, altura_der)

    def _balance(self, node):
        """
        Calcula el FACTOR DE BALANCE de un nodo.
        
        Parámetros:
        -----------
        node : AVLNode o None
            El nodo a evaluar
        
        Retorna:
        --------
        int : Factor de balance (altura_izq - altura_der)
        
        Interpretación:
        ---------------
        - FB = 0  → Perfectamente balanceado
        - FB = 1  → Ligeramente más alto a la izquierda (OK)
        - FB = -1 → Ligeramente más alto a la derecha (OK)
        - FB > 1  → Desbalanceado a la izquierda (NECESITA ROTACIÓN)
        - FB < -1 → Desbalanceado a la derecha (NECESITA ROTACIÓN)
        """
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    # ==================== ROTACIONES ====================
    # Las rotaciones son operaciones que reorganizan los nodos
    # para restaurar el balance del árbol.
    # Hay 2 rotaciones básicas: derecha e izquierda.

    def _rotate_right(self, y):
        """
        Realiza una ROTACIÓN DERECHA en el nodo y.
        
        Cuándo usar:
        ------------
        Cuando el árbol está "pesado hacia la izquierda" (FB > 1)
        
        Transformación:
        ---------------
              y                    x
             / \                  / \
            x   C    ------>     A   y
           / \                      / \
          A   B                    B   C
        
        Parámetros:
        -----------
        y : AVLNode
            El nodo desbalanceado (raíz del subárbol a rotar)
        
        Retorna:
        --------
        AVLNode : La nueva raíz del subárbol (x)
        """
        # Guardamos referencias a los nodos involucrados
        x = y.left      # x será la nueva raíz
        B = x.right     # B es el subárbol que cambiará de padre
        
        # Realizamos la rotación
        x.right = y     # y baja y se convierte en hijo derecho de x
        y.left = B      # B se convierte en hijo izquierdo de y
        
        # Actualizamos alturas (¡EL ORDEN IMPORTA!)
        # Primero y (porque ahora está más abajo)
        # Luego x (la nueva raíz, que depende de y)
        self._update_height(y)
        self._update_height(x)
        
        return x  # Devolvemos la nueva raíz del subárbol

    def _rotate_left(self, x):
        """
        Realiza una ROTACIÓN IZQUIERDA en el nodo x.
        
        Cuándo usar:
        ------------
        Cuando el árbol está "pesado hacia la derecha" (FB < -1)
        
        Transformación:
        ---------------
            x                      y
           / \                    / \
          A   y      ------>     x   C
             / \                / \
            B   C              A   B
        
        Parámetros:
        -----------
        x : AVLNode
            El nodo desbalanceado (raíz del subárbol a rotar)
        
        Retorna:
        --------
        AVLNode : La nueva raíz del subárbol (y)
        """
        # Guardamos referencias a los nodos involucrados
        y = x.right     # y será la nueva raíz
        B = y.left      # B es el subárbol que cambiará de padre
        
        # Realizamos la rotación
        y.left = x      # x baja y se convierte en hijo izquierdo de y
        x.right = B     # B se convierte en hijo derecho de x
        
        # Actualizamos alturas (¡EL ORDEN IMPORTA!)
        # Primero x (porque ahora está más abajo)
        # Luego y (la nueva raíz, que depende de x)
        self._update_height(x)
        self._update_height(y)
        
        return y  # Devolvemos la nueva raíz del subárbol

    # ==================== INSERCIÓN ====================

    def insert(self, key, value):
        """
        Inserta un nuevo par (clave, valor) en el árbol.
        
        Parámetros:
        -----------
        key : comparable
            La clave de ordenación
        value : any
            El valor a almacenar
        
        El árbol se rebalancea automáticamente si es necesario.
        """
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        """
        Método recursivo que realiza la inserción y rebalanceo.
        
        Parámetros:
        -----------
        node : AVLNode o None
            La raíz del subárbol actual
        key : comparable
            La clave a insertar
        value : any
            El valor a insertar
        
        Retorna:
        --------
        AVLNode : La raíz del subárbol (posiblemente nueva tras rotación)
        """
        # ===== CASO BASE: Llegamos a una posición vacía =====
        if not node:
            return AVLNode(key, value)  # Creamos el nuevo nodo aquí

        # ===== PASO RECURSIVO: Navegamos hacia la posición correcta =====
        if key < node.key:
            # La clave es menor → va al subárbol izquierdo
            node.left = self._insert(node.left, key, value)
        else:
            # La clave es mayor o igual → va al subárbol derecho
            # (permitimos claves duplicadas, van a la derecha)
            node.right = self._insert(node.right, key, value)

        # ===== ACTUALIZACIÓN Y BALANCEO (al "subir" de la recursión) =====
        
        # Actualizamos la altura de este nodo
        self._update_height(node)
        
        # Calculamos el factor de balance
        balance = self._balance(node)

        # ===== CASO 1: Izquierda-Izquierda (LL) =====
        # El árbol está pesado a la izquierda Y el nuevo nodo
        # fue insertado en el subárbol izquierdo del hijo izquierdo
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # ===== CASO 2: Derecha-Derecha (RR) =====
        # El árbol está pesado a la derecha Y el nuevo nodo
        # fue insertado en el subárbol derecho del hijo derecho
        if balance < -1 and key >= node.right.key:
            return self._rotate_left(node)

        # ===== CASO 3: Izquierda-Derecha (LR) =====
        # El árbol está pesado a la izquierda PERO el nuevo nodo
        # fue insertado en el subárbol derecho del hijo izquierdo
        # Requiere DOBLE ROTACIÓN: izquierda + derecha
        if balance > 1 and key >= node.left.key:
            node.left = self._rotate_left(node.left)  # Primero rotamos el hijo
            return self._rotate_right(node)            # Luego rotamos este nodo

        # ===== CASO 4: Derecha-Izquierda (RL) =====
        # El árbol está pesado a la derecha PERO el nuevo nodo
        # fue insertado en el subárbol izquierdo del hijo derecho
        # Requiere DOBLE ROTACIÓN: derecha + izquierda
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)  # Primero rotamos el hijo
            return self._rotate_left(node)                # Luego rotamos este nodo

        # Si no hubo desbalance, devolvemos el nodo sin cambios
        return node

    # ==================== EXTRACCIÓN DEL MÍNIMO ====================

    def extract_min(self):
        """
        Extrae y devuelve el elemento con la CLAVE MÍNIMA.
        
        Retorna:
        --------
        tuple : (clave, valor) del elemento mínimo
        None : Si el árbol está vacío
        
        Esta es la operación clave para usar el AVL como cola de prioridad.
        En Dijkstra, siempre queremos procesar el nodo con menor distancia.
        """
        if not self.root:
            return None
        
        # Extraemos el mínimo y actualizamos la raíz
        self.root, min_node = self._extract_min(self.root)
        
        return min_node.key, min_node.value

    def _extract_min(self, node):
        """
        Método recursivo que extrae el nodo mínimo y rebalancea.
        
        Parámetros:
        -----------
        node : AVLNode
            La raíz del subárbol actual
        
        Retorna:
        --------
        tuple : (nueva_raíz_del_subárbol, nodo_mínimo_extraído)
        
        Nota:
        -----
        El mínimo SIEMPRE está en el extremo izquierdo del árbol.
        Bajamos por la izquierda hasta encontrar un nodo sin hijo izquierdo.
        """
        # ===== CASO BASE: Este es el nodo mínimo =====
        # Si no tiene hijo izquierdo, este es el mínimo
        if not node.left:
            # Devolvemos:
            # - node.right como reemplazo (puede ser None)
            # - node como el mínimo encontrado
            return node.right, node

        # ===== PASO RECURSIVO: Seguimos bajando por la izquierda =====
        node.left, min_node = self._extract_min(node.left)
        
        # ===== REBALANCEO (al "subir" de la recursión) =====
        self._update_height(node)
        balance = self._balance(node)

        # Después de extraer de la izquierda, el árbol puede quedar
        # pesado hacia la derecha (balance < -1)
        
        if balance < -1:
            # Verificamos qué tipo de rotación necesitamos
            if self._balance(node.right) <= 0:
                # Caso RR: rotación izquierda simple
                node = self._rotate_left(node)
            else:
                # Caso RL: doble rotación
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
        elif balance > 1:
            # También podría desbalancearse a la izquierda
            if self._balance(node.left) >= 0:
                # Caso LL: rotación derecha simple
                node = self._rotate_right(node)
            else:
                # Caso LR: doble rotación
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)

        return node, min_node

    def is_empty(self):
        """
        Verifica si el árbol está vacío.
        
        Retorna:
        --------
        bool : True si está vacío, False si tiene elementos
        """
        return self.root is None


# ===========================================================
#              TDA: DIJKSTRA ALGORITHM
# ===========================================================
# El algoritmo de Dijkstra encuentra el CAMINO MÁS CORTO desde
# un nodo origen hacia TODOS los demás nodos del grafo.
# 
# Requisitos:
# - Grafo con pesos NO NEGATIVOS (importante!)
# - Grafo dirigido o no dirigido
# 
# Complejidad con AVL: O((V + E) * log V)
#   V = número de vértices (nodos)
#   E = número de aristas
# ===========================================================

class Dijkstra:
    def __init__(self, graph):
        """
        Constructor del algoritmo de Dijkstra.
        
        Parámetros:
        -----------
        graph : Graph
            El grafo sobre el cual ejecutar el algoritmo
        """
        self.graph = graph  # Guardamos referencia al grafo

    def run(self, start_name):
        """
        Ejecuta el algoritmo de Dijkstra desde un nodo origen.
        
        Parámetros:
        -----------
        start_name : str
            Nombre del nodo desde el cual calcular distancias
        
        Raises:
        -------
        ValueError : Si el nodo origen no existe en el grafo
        
        Después de ejecutar:
        -------------------
        Cada nodo tendrá actualizado:
        - distance: distancia mínima desde el origen
        - previous: nodo anterior en el camino más corto
        """
        # ===== PASO 1: Inicialización =====
        # Reseteamos todas las distancias a infinito y previous a None
        self.graph.reset_distances()
        
        # Obtenemos el nodo de inicio
        start = self.graph.get_node(start_name)
        if not start:
            raise ValueError(f"Nodo '{start_name}' no existe")

        # La distancia del origen a sí mismo es 0
        start.distance = 0
        
        # ===== PASO 2: Creamos la cola de prioridad =====
        # Usamos el árbol AVL como cola de prioridad
        # Los elementos se ordenan por distancia (menor primero)
        pq = AVLTree()
        pq.insert(0, start)  # Insertamos el origen con distancia 0

        # ===== PASO 3: Procesamos nodos hasta vaciar la cola =====
        while not pq.is_empty():
            # Extraemos el nodo con MENOR distancia
            dist, node = pq.extract_min()
            
            # ===== OPTIMIZACIÓN: Saltamos nodos obsoletos =====
            # ¿Por qué puede haber nodos obsoletos?
            # Porque insertamos el mismo nodo varias veces cuando
            # encontramos caminos más cortos. Las versiones anteriores
            # (con distancias mayores) siguen en la cola.
            # Si dist > node.distance, ya procesamos este nodo con
            # una distancia menor, así que lo ignoramos.
            if dist > node.distance:
                continue

            # ===== PASO 4: Exploramos todos los vecinos =====
            for edge in node.edges:
                neighbor = edge.destination  # Nodo vecino
                
                # Calculamos la distancia total hasta el vecino
                # = distancia hasta el nodo actual + peso de la arista
                new_dist = node.distance + edge.weight

                # ===== RELAJACIÓN: ¿Encontramos un camino mejor? =====
                if new_dist < neighbor.distance:
                    # ¡Sí! Actualizamos la distancia del vecino
                    neighbor.distance = new_dist
                    
                    # Recordamos que llegamos al vecino desde este nodo
                    # (para reconstruir el camino después)
                    neighbor.previous = node
                    
                    # Añadimos el vecino a la cola de prioridad
                    # con su nueva distancia
                    pq.insert(new_dist, neighbor)

    def get_path(self, destination_name):
        """
        Reconstruye el camino más corto hacia un destino.
        
        Parámetros:
        -----------
        destination_name : str
            Nombre del nodo destino
        
        Retorna:
        --------
        list : Lista de nombres de nodos en orden [origen, ..., destino]
               Lista vacía si no hay camino o el nodo no existe
        
        Nota:
        -----
        Debe llamarse DESPUÉS de ejecutar run()
        """
        # Obtenemos el nodo destino
        dest = self.graph.get_node(destination_name)
        
        # Si no existe o no es alcanzable (distancia infinita)
        if not dest or dest.distance == float('inf'):
            return []

        # ===== RECONSTRUCCIÓN DEL CAMINO =====
        # Empezamos desde el destino y vamos hacia atrás
        # siguiendo los enlaces "previous"
        path = []
        current = dest
        
        while current:
            path.append(current.name)  # Añadimos el nodo actual al camino
            current = current.previous  # Nos movemos al nodo anterior
        
        # El camino está al revés (destino → origen)
        # Lo invertimos para tener (origen → destino)
        return path[::-1]

    def get_distance(self, destination_name):
        """
        Obtiene la distancia mínima hacia un destino.
        
        Parámetros:
        -----------
        destination_name : str
            Nombre del nodo destino
        
        Retorna:
        --------
        float : La distancia mínima desde el origen
                float('inf') si no hay camino o el nodo no existe
        
        Nota:
        -----
        Debe llamarse DESPUÉS de ejecutar run()
        """
        node = self.graph.get_node(destination_name)
        return node.distance if node else float('inf')


# ===========================================================
#                    EJEMPLO DE USO
# ===========================================================
# Creamos un grafo de ejemplo y ejecutamos Dijkstra para
# encontrar los caminos más cortos desde el nodo "A".
# ===========================================================

if __name__ == "__main__":
    # ===== PASO 1: Crear el grafo =====
    g = Graph()

    # ===== PASO 2: Añadir las aristas (conexiones) =====
    # Cada llamada crea una conexión dirigida: origen → destino con peso
    # 
    # Visualización del grafo:
    #
    #           4
    #      A ------→ B
    #      |         |
    #    2 |    1    | 5
    #      ↓   ↗     ↓
    #      C ------→ D
    #      |         |
    #   10 |    2    | 6
    #      ↓   ↗     ↓
    #      E ←------ F
    #           3
    #
    g.add_edge("A", "B", 4)   # A → B con costo 4
    g.add_edge("A", "C", 2)   # A → C con costo 2
    g.add_edge("C", "B", 1)   # C → B con costo 1 (atajo!)
    g.add_edge("B", "D", 5)   # B → D con costo 5
    g.add_edge("C", "D", 8)   # C → D con costo 8
    g.add_edge("C", "E", 10)  # C → E con costo 10
    g.add_edge("D", "E", 2)   # D → E con costo 2
    g.add_edge("D", "F", 6)   # D → F con costo 6
    g.add_edge("E", "F", 3)   # E → F con costo 3

    # ===== PASO 3: Ejecutar Dijkstra desde "A" =====
    dijkstra = Dijkstra(g)
    dijkstra.run("A")

    # ===== PASO 4: Mostrar resultados =====
    print("=" * 50)
    print("ALGORITMO DE DIJKSTRA - RESULTADOS")
    print("=" * 50)
    print(f"\nNodo origen: A\n")
    
    print("DISTANCIAS MÍNIMAS DESDE A:")
    print("-" * 30)
    for name in sorted(g.nodes.keys()):
        distance = g.get_node(name).distance
        # Formateamos infinito de forma legible
        dist_str = str(distance) if distance != float('inf') else "∞ (inalcanzable)"
        print(f"  A → {name}: {dist_str}")

    print("\nCAMINOS MÁS CORTOS:")
    print("-" * 30)
    for dest in ["B", "C", "D", "E", "F"]:
        path = dijkstra.get_path(dest)
        dist = dijkstra.get_distance(dest)
        
        if path:
            path_str = " → ".join(path)
            print(f"  A → {dest}: {path_str}")
            print(f"          Distancia total: {dist}")
        else:
            print(f"  A → {dest}: No hay camino disponible")
        print()

    # ===== EJEMPLO ADICIONAL: Verificar camino específico =====
    print("=" * 50)
    print("ANÁLISIS DETALLADO: Camino A → F")
    print("=" * 50)
    
    path_to_f = dijkstra.get_path("F")
    if path_to_f:
        print(f"\nCamino encontrado: {' → '.join(path_to_f)}")
        print(f"Distancia total: {dijkstra.get_distance('F')}")
        
        print("\nDesglose paso a paso:")
        for i in range(len(path_to_f) - 1):
            current = g.get_node(path_to_f[i])
            next_name = path_to_f[i + 1]
            
            # Encontramos el peso de la arista
            for edge in current.edges:
                if edge.destination.name == next_name:
                    print(f"  {current.name} → {next_name}: +{edge.weight}")
                    break
