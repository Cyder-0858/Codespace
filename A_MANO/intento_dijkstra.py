class arista:
    def __init__(self,origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

class nodo:
    def __init__selg(self, nombre):
        self.nombre = nombre
        self.arista = []
        self.distancia = float("inf")
        self.nodo_anterior = None
    
    def agregar_arista(self,origen, destino, peso):
        self.aristas.append(arista(origen, destino, peso)) 

    def reiniciar(self):
        self.distancia = float("inf")
        self.nodo_anterior = None

class grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self,nombre):
        if nombre not in self.nodos:
            self.nodos[nombe]