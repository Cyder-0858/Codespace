pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 5

n = len(pesos)

class item:
    def __init__(self, nombre, peso, prioridad):
        self.nombre = nombre
        self.peso = peso
        self.prioridad = prioridad  

        def __rep__(self):
            return f"{self.nombre}: peso {self.peso}, prioridad {self.prioridad}"
        
class nodo:
    def __init__(self, index, peso, prioridad):
        self.index = index
        self.peso = peso
        self.prioridad = prioridad

        def add_arista(self, edge):
            self.aristas.append(edge)

class arista:
    def __init__(self, next_node, decision):
        self.next_node = next_node
        self.decision = decision


class graph:
    def__init__(self, itmes, capacidad):
        self.items = items
        self.capacidad = capacidad
        self.start = nodo(0, 0, 0)
        self.nodes = [self.start]
    
    def build(self):
        queue = [self.start]
        
        while queue:
            current = queue.pop
            if current.index == len(self.items):
                continue

            items = self.items[current.index]

            skip_node = nodo(current.index + 1, current.peso, current.prioridad)
            self.nodos.append(skip_node)
            current.add_arista(arista(skip_node, "skip"))
            queue.append(skip_node)

            if current.weight + item.peso <= self.capacidad:
                take_node = nodo(current.index + 1, current.peso + item.peso, current.prioridad + item.prioridad)
                self.nodos.append(take_node)
                current.add_arista(arista(take_node, "take"))
                queue.append(take_node)

class knapsacksolver:
    def __init__(self, graph):
        self.graph = graph

    def solve(self):

        best_priority = -1
        best_node = None

        stack = [self.graph.start]

        while stack:
            current = stack.pop()

            if current.index == len(self.graph.items):
                if current.prioridad > best_priority:
                    best_priority = current.prioridad
                    best_node = current

            for edge in current.aristas:
                stack.append(edge.next_node)

        path = []
        node = self.graph.start

        while node.index < len(self.graph.items):
            for edge in node.aristas:
                if edge.next_node == node.index + 1:
                    path.append(edge.decision)
                    node = edge.next_node
                    break

