class Node:
    def __init__(self, index, weight, priority):
        self.index = index        # índice del objeto considerado
        self.weight = weight      # peso acumulado
        self.priority = priority  # prioridad acumulada
        
        self.edges = []           # aristas hacia nodos hijos

        # Datos para reconstrucción elegante
        self.parent = None        # nodo padre
        self.action = None        # "take" o "skip"

    def add_edge(self, edge):
        self.edges.append(edge)
