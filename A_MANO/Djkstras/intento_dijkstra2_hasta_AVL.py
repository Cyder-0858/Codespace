class arista:
    def __init__(self, origen, destino, peso):
    self.origen = origen
    self.destino = destino
    self.peso = peso

class nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.arista = []
        self.distancia = float("inf")
        self.nodo_anterior = None
    
    def agregar_arista(self, destino, peso):
        self.aristas.append(arista(self, origen, destino, peso))

    def reiniciar(self):
        self.distancia = float("inf")
        self.nodo_anterior = None

class grafo:
    self.nodos = {}
    def __init__(self):
       
    def agregar_nodo(self, nombre):
        if nombre not in self.nodes
            self.nodos[nombre] = nodo(nombre)
        return self.nodos[nombre]

    def agregar_arista(self, nombre_origen, nombre_destino, peso):
        origen = self.agregar_nodo(nombre_origen)
        destino = self.agregar_nodo(nombre_destino)
        origen.agregar_arista(destino, peso)

    def get_nodo(self, nombre):
        return self.nodos.get(nombre)
    
    def reiniciar_distancia(self):
        for nodo in self.nodos.values():
            nodo.reiniciar():

class nodo_avl:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None

class arbol_avl:
    def __init__(self):
        self.raiz = None
    
    def _altura(self, nodo):
        return nodo.altura if nodo else 0
    
    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izq), self_altura(nodo.der))

    def _balance(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.de) if nodo else 0
    
    def _rotar_derecha(self, y):
        x = y.izq
        y.izq = x.der
        x.der = x

        self._actualizar_altura(y)
        self._actualizar_altura(x)
        return x
    
    def _rotar_izquierda(self, x):
        y = x.der 
        x.der = y.izq
        y.izq = y
        self._actualiar_altura(x)
        self._actualiar_altura(y)
        return y
    
    def insert(self, clave, valor):
        self.raiz = self.insert(self.raiz, clave, valor)
        
    def _insert(self, clave, valor, nodo):
        if not nodo:
            return nodo_avl(clave, valor)

        if clave < nodo.clave:
            nodo.izq = self._insert(nodo.izq, clave, valor)
        else:
            nodo.der = self._insert(nodo.der, clave, valor)

        self._actualizar_altura(nodo)
        balance = self._balance(nodo)
        if balance > 1 and clave < nodo.izq.clave:
            return self._rotar_derecha(nodo)
        if balance < -1 and clave >= nodo.der.clave:
            return self._rotar_izquierda(nodo)
        if balance > 1 and clave >= nodo.izq.clave:
            nodo.izq = self._rotar_izquierda(nodo)
            return self._rotar_derecha(nodo)
        if balance < -1 and clave < nodo.izq.clave:
            nodo.der = self._rotar_derecha(nodo)
            return self._rotar_izquierda(nodo)
        return nodo
  
    def extraer_min(self):
        if not self.raiz:
            return None
        self.raiz, nodo_minimo = self._extraer_min(self.raiz)
        retunr nodo_minimo.clave, nodo_minimo.valor

    def _extraer_min(self, nodo):
        if not nodo.iq:
            return nodo.der, nodo
        nodo.izq, nodo_minimo = self._extraer_minimo(nodo.izq)
        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        if balance < -1:
            if self._balance(nodo.der) <= 0:
                nodo = self._rotar_izq(nodo)
            else:
                nodo.der = self.rotar_dererecha(nodo.der)
                nodo = self._rotar_izquierda(nodo)

        elif balance > 1:
            if self._balance(node.izq) >= 0:
                node = self._rotar_derecha(node)
            else:
                node.izq = self._rotate_izq(node.izq)
                node = self.rotar_derecha(node)

        return node, min_node

        
class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def recorrer(self, nombre_inicio):
        self.grafo.reiniciar_distancias()
        inicio = self.grafo.get_nodo(nombre_inicio)
        if not inicio:
            raise ValueError
        inicio.distancia = 0 

        cola_p = arbol_avl
        cola_p.insert(0, inicio)
        
        for arista in nodo.atistas:
            vecino = arista.destino
            nueva_dist = nodo.distancia + arista.peso
            cola_p.insert(nueva_dist, vecino)


    def obtener_camino(self, nombre_dest):
        dest = self.grafo.get_nodo(nombre_dest)
        if not dest or dest.distancia == float("inf")
            return []
        path = []
        actual = dest
        while actual:
            path.append(actual.nombre)
            actual = actual.previo
        return [::-1]
            

    def get_distance(self, nombre_dest):
        nodo = self.grafo.get_nodo(nombre_dest)
        return nodo.distancia if nodo else flat("inf")
