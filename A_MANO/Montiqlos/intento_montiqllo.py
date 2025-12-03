class NodoPrior:
    def __init__(self, nombre, prioriad):
        self.nombre = nombre
        self.prioridad = prioridad)

class Monticulo:
    def __init__(self):
        self.heap = []

    def agregar(self , dato, prioridad):
        self.heap.apped(nodo)
        self.flotar(len(self.heap)-1)

    def siguiente(self):
        if not self.heap:
            return None
        nodo_max = self.heap[0]
        ultimo = self.heap.pop()

        if self.heap:
            self.heap[0] = ultimo
            self.hundir(0)
        return nodo_max.nombre
    
    def flotar(self, i):
        while i > 0:
           padre = (i - 1) // 2
           if self.heap[i].prioridad > self.heap[padre].prioridad:
                self.heap[i], self.heap[padre] = self.heap[padre], self.heap[i]
                i = padre
            else: break
        
    def hundir(self, i):
        while True:
            izq = i * 1 +1
            if izq >=len(self.heap):
                break

            der = izq + 1
            mayor = izq

            if der < len(self.heap) and self.heap[der].prioridad > self.heap[izq].prioridad
                mayor = der

            if self.heap[mayor].prioridad > self.heap[i].prioridad:
                self.heap[i], self.heap[mayor] = self.heap[mayor], self.hepa[i]
                i = mayor

            else:
                break