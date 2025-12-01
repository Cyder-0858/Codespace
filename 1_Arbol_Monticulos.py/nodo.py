# -------------------------------------------------------
# TDA: Nodo (Estado genérico del grafo)
# -------------------------------------------------------
class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value        # El criterio de ordenamiento del montículo (costo, prioridad, etc.)
        self.edges = []           # Lista de aristas
        
        # Datos para reconstrucción del camino
        self.parent = None

    def add_edge(self, edge):
        self.edges.append(edge)

    # Método mágico necesario para que el Heap sepa comparar nodos.
    # Por defecto heapq en Python es Min-Heap (menor valor sale primero).
    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return f"Node({self.name}, Val:{self.value})"
