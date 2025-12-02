# -------------------------------------------------------
# PRUEBA GENÉRICA
# -------------------------------------------------------

# 1. Instanciación del Grafo
graph = Graph()

# 2. Creación de Nodos (Nombre, Prioridad/Costo)
# Nota: Como es Min-Heap, '5' saldrá antes que '10'
n_root = Node("Raiz", 0)
n_a = Node("Nodo A", 50)
n_b = Node("Nodo B", 10)  # Prioridad más alta (valor menor)
n_c = Node("Nodo C", 30)
n_d = Node("Nodo D", 5)   # Prioridad máxima

# Añadir al grafo
graph.add_node(n_root)
graph.set_start(n_root)

# 3. Conexiones (Aristas)
# Raiz -> A y B
n_root.add_edge(Edge(n_a))
n_root.add_edge(Edge(n_b))

# B -> D (Camino prometedor)
n_b.add_edge(Edge(n_d))

# A -> C
n_a.add_edge(Edge(n_c))

# 4. Ejecutar Algoritmo
algo = HeapAlgorithm(graph)
recorrido = algo.run()

print("\n===========================")
print("Orden final de visita (Por Prioridad):")
print([n.name for n in recorrido])
print("===========================")