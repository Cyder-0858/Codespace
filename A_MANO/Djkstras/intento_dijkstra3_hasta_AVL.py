class arista:
    def __init__(self, origen, destino, peso)
        self.origen = origen
        self.destino = destino
        self.peso = peso

class nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aristas = []
        self.distancia = float("inf")
        self.nodo_previo = None

        def agregar_aristas(self, destino, peso):
            if nombre not in self.aristas:
                self.nombre.append(nodo.agregar_arista(destino, peso))

        def reiniciar(self):
            self.distancia = float("inf")
            self.nodo_previo = None
        
class grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[name] = grafo(nombre)
        
    def agregar_arista(self, origen, destino, peso):
        origen = self.agregar_nodo(origen)
        destino = self.agregar_nodo(destino)
        origen.agregar_arista(destino, peso)

    def get_nodo(self, nombre):
        return self.get_nodo(nombre)

    def reiniciar_distanca(self):
        for nodo in self.nodos.values()
            self.reiniciar()

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
    def altura(self, nodo)
        return nodo.altura if nodo else 0
    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izq)+ self.altura(nodo.derecha))
    def balance (self, nodo):
        return self.altura(nodo.izq)-self.altua(nodo.der) if nodo else 0
    def rotar_der(self, y)
        x = y.izq
        y.izq = x.der
        x.der = y
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return y
    def rotar_izq(self, x)
        y = x.der
        x.der = y.izq
        y.izq = x
        self.actualizar_altura(x)
        self.actualizar_altura(y)
    
    def insertar(self, valor, clave):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, valor, clave):
        if not nodo:
            return nodo_avl(clave, valor)
        
        if clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave, valor)
        else:
            nodo.der = sel._insertar(nodo.der, clave, valor)

        self.actualizar_altura(nodo)
        balance = self.balance(nodo)

        if balance > 1 and key < nodo.izq.clave:
            return self.rotar_der(nodo)
        if balance < -1 and key >= nodo.der.clave:
            return self.rotar_izq(nodo)
        if balance > 1 and key >= nodo.izq.clave:
            nodo.izq = self.rotar_izq(nodo)
            return self.rotar.der(nodo)
        if balance < -1 and clave < nodo.der.clave:
            nodo.der = self.rotar_der(nodo)
            return self.rotar_izq(nodo)
        return nodo
    
    def extraer_min(self):
        if not self.raiz:
            return None
        self.raiz, nodo_min = self._extraer_min(self.raiz)
        return self.nodo_min, nodo_min.valor
    
    def _extraer_min(self, nodo):
        if not nodo.izq:
            return nodo.der, nodo
        nodo.izq, nodo_min = self._extraer_min(nodo.izq)
        self._actualizar_altura(nodo)
        balance = self._balance(nodo)

        if balance < -1:
            if self._balance(nodo.der) <= 0:
                nodo = self.rotar_der(nodo.der)
            else:
                nodo.der = self.rotar_der(nodo.der)
                nodo = self.rotar_izq(nodo)
            if self._balance(nodo.izq) > 0:
                nodo = self.rotar_izq(nodo.izq)
            else:
                nodo.izq = self.rotar_izq(nodo.izq)
                nodo = self.rotar_der(nodo)
            return nodo, nodo_min
        
    def is_empty(self):
        return self.raiz is None



class dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def run(self, inicio_nombre):
        self.grafo.reiniciar_distancia()
        inicio = self.grafo.get_nodo(inicio_nombre)
        if not inicio:
            raise ValueError
        
        inicio.distancia = 0
        cola_prior = arbol_avl
        cola_prior.insertar(0, inicio_nombre)

        while cola_prior.is_empty()
            dist, nodo = cola_prior.extraer_min()

            if dist > nodo.distancia
                continue
            for arista in nodo.aristas
                vecino = 
                nueva_dist = 
                if nueva_dist < vecino #...

    def obtener_camino(self, nombre_dest)
        dest = self.grafo.get_nodo(nombre_dest)
        if not dest or dest.distancia == float("inf")
            return []
        path = []
        current = dest
        while current:
            path.append(current.name)
            current = current.previo
        return [::-1]

    def get_distancia(self, nombre_dest)
        nodo = self.grafo.get_nodo(nombre_dest)
        return nodo.distancia

