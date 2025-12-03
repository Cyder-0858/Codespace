class arista:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

class nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aristas = []
        self.distancia = float("inf")
        self.nodo_previo = None

    def agregar_aristaaaaaaaaaaaaa(self, destino, peso):
        self.aristas.append(arista(destino, peso))

    def reiniciar(self):
        self.distancia = float("inf")
        self.nodo_previo = None

class grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, nombre):
        if nodo not in self.nodos:
            self.nodos[nombre] = nodo(nombre)
            return self.nodos[nombre]
        
    def agregar_arista(self, nombre_origen, nombre_destino, peso):
        origen = self.agregar_arista(nombre_origen)
        destino = self.agregar_arista(nombre_destino)
        origen.agregar_arista(destino, peso)

    def get_nodo(self, nombre):
        return self.nodo(nombre)
    
    def reiniciar_distancia(self):
        for nodo in self.nodo.values():
            nodo.reiniciar()

class nodo_avl:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None

class arbol_avl:
    