# -------------------------------------------------------
# TDA: Grafo (Estructura contenedora)
# -------------------------------------------------------
class Graph:
    def __init__(self):
        self.nodes = [] # Lista de nodos registrados
        self.start = None

    def add_node(self, node):
        self.nodes.append(node)
        
    def set_start(self, node):
        self.start = node


