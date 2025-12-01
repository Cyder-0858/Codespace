# -------------------------------------------------------
# TDA: Edge (Transición entre nodos)
# -------------------------------------------------------
class Edge:
    def __init__(self, next_node, cost=0):
        self.next_node = next_node
        self.cost = cost          # Peso o costo de la transición
