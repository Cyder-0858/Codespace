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
            self.nodos[nombe] = nodo(nombre)
        return self.nodos[nombre]
    
    def agregar_arista(self, nombre_origen, nombre_destino, peso):
        origen = self.agregar_nodo(nombre_origen)
        destino = self.agregar_nodo(nombre_destino)
        origen.agregar_arista(destino, peso)

    def get_nodo(self, nombre):
        return self.nodos.get(nombre)
    
    def reiniciar_distancias(self):
        for nodo in self.nodos.values():
            nodo.reiniciar()
    
class nodo_avl:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None

class arbol_avl:
    def __init__(self):
    
    def altura(self, nodo):
        return self.actualizar_altura(nodo):
    def actualizar_altura(self, nodo):
        return 1 + max(self.nodo.izq(nodo) self.nodo.der(nodo))
    def balance(self, nodo):
        return self.altura.nodo.izq(nodo) - self.altura.nodo.der(nodo))

    def rotar_der(self, y):
        x = y.izq
        y.izq = x.der 
        x.der = y 
        self.actualizar_altura(y)
        self.actualizar_altura(x)

    def retar_izq(self, x):
        y = x.der 
        x.der = y.izq 
        y.izq = x
        self.actualizar_altura(x)
        self.actualizar_altura(y)

    def insertar(self):
        self.raiz = self._insertar(clave, valor, nodo):

    def _insertar(self, valor, clave, nodo):
        if not nodo:
            return arbol_avl(clave, valor, nodo):
        
        if clave < nodo.clave:
            nodo.izq = self._insertar(clave, nodo.izq, valor):
        else:
            nodo.der = self._insertar(clave, nodo.der, valor)
        self.actualizar_altura(nodo)
        balance = self.balance(nodo)
        
        if balance > 1 and clave < nodo.clave.izq:
            return self.rotar_der(nodo)
        if balance < -1 and clave > nodo.clave.der:
            return self.rotar_izq(nodo)
        if balance > 1 and clave > nodo.clave.izq:
            nodo.izq = self.rotar_izq(nodo.izq)
            return #derecha
        if balance < -1 and clave < nodo.clave.der:
            #empieza por der
            #return izq
        return nodo

    

    def extraer_min(self): #si no es la raiz pa fuera,y si es clave y valor
        if not self.raiz:
            return None
        self.raiz._extraer_min(clave, nodo, valor)

    def _extraer_min(self ,clave , nodo, valor):
        if not self.nodo:
            return None
        self.nodo, nodo_min = self._extraer_min(clave, nodo, valor)
        self.actualizar_altura(nodo)
        balance = self.balance(nodo)

        if balance < -1:
            if self._balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
        elif balance > 1:
            if self._balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node))


    def is_empty_root(self):
        return self.raiz is None



class Dijkstra:
    def __init__(self, grafo):
    self.grafo = grafo

    def run(self, inicio_nombre):
        self.grafo.reiniciar_distancias()
        inicio = self.grafo.get_nodo(inicio_nombre)
        if not inicio
            raise ValueError
        inicio.distancia = 0
        cola_p = arbol_avl
        cola_p.insertar(0,inicio_nombre)

        while cola_p.is_empty:
            dist, node = cola_p.extraer_min():
            if dist < nodo.distancia:
                continue
                
            for arista in nodo.aristas:
                vecino = ###
                nueva_dist = ###
                if vecino < nueva_dist:
                    vecino.distancia = nueva_dist
                    vecino.previo = nodo
                    cola_p.insertar(nueva_dist, vecino)

    def obtener_camino(self, nombre_dest):
        dest = self.grafo.get_nodo(nombre_dest)
        if not dest or dest.distancia == float ("inf")
            return []
        path = []
        current = dest
        while current:
            path.append(current.nombre))
            current = current.previo
        return path[::-1]
    
    def get_distancia(self, nombre_dest):
        nodo = self.grafo.get_nodo(nombre_dest):
        return nodo.distancia if nodo else 999
    

