# -------------------------------------------------------
# Solucionador de la mochila mediante grafo
# -------------------------------------------------------

class KnapsackSolver:
    def __init__(self, graph):
        self.graph = graph

    def solve(self):

        best_node = None
        best_priority = -1

        stack = [self.graph.start]

        # -----------------------------------------------
        # Buscar el nodo con mayor prioridad
        # -----------------------------------------------
        while stack:
            current = stack.pop()

            # nodo terminal
            if current.index == len(self.graph.items):
                if current.priority > best_priority:
                    best_priority = current.priority
                    best_node = current

            for edge in current.edges:
                stack.append(edge.next_node)

        # -----------------------------------------------
        # ⭐ Reconstrucción elegante mediante parent
        # -----------------------------------------------
        path = []
        node = best_node

        while node.parent is not None:
            item_index = node.parent.index
            item = self.graph.items[item_index]

            path.append((node.action, item))
            node = node.parent

        path.reverse()
        return path, best_priority
