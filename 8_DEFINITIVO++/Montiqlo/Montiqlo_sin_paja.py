class NodoPrioridad:
    def __init__(self, prioridad, dato):
        self.prioridad = prioridad
        self.dato = dato


class Monticulo:
    def __init__(self):
        self.heap = []  # Capacidad ilimitada
    
    def agregar(self, dato, prioridad):
        nodo = NodoPrioridad(prioridad, dato)
        self.heap.append(nodo)
        self._flotar(len(self.heap) - 1)
    
    def siguiente(self):
        if not self.heap:
            return None
        
        nodo_max = self.heap[0]
        ultimo = self.heap.
        ()
        
        if self.heap:
            self.heap[0] = ultimo
            self._hundir(0)
        
        return nodo_max.dato
    
    def _flotar(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self.heap[i].prioridad > self.heap[padre].prioridad:
                self.heap[i], self.heap[padre] = self.heap[padre], self.heap[i]
                i = padre
            else:
                break
    
    def _hundir(self, i):
        while True:
            izq = 2 * i + 1
            if izq >= len(self.heap):
                break
            
            der = izq + 1
            mayor = izq
            
            if der < len(self.heap) and self.heap[der].prioridad > self.heap[izq].prioridad:
                mayor = der
            
            if self.heap[mayor].prioridad > self.heap[i].prioridad:
                self.heap[i], self.heap[mayor] = self.heap[mayor], self.heap[i]
                i = mayor
            else:
                break