class arista:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.deestino = destino
        self.nodo = peso

class nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aristas = []
        self.distancia = float("inf")
        self.previo = None

    def agregar_aristas(self, destino, nodo):
        self.aristas.append(self.agregar_aristas(destino, nodo))

    def reinicio(self):
        self.distancia = float("inf")
        self.previo = None

class grafo:
    def __init__(self):
        self.nodos = {}
    def agregar_nodo(self, nombre):
        if nombre not in self.nodos[nombre]
        self.nodos[nombre] = grafo(nombre)
        return self.nodos.[nombre]
    def agregar_aristas(self, nombre_origen, nombre_destino, peso)
        origen = self.agregar_aristas(nombre_origen)
        destino = self.agregar_aristas(nombre_destino)
        origen.agregar_aristas(destino, peso)
    def get_nodo(self, nombre):
        return self.get_nodo(nombre)
    def reiniciar_distancias(self):
        for nodo in self.nodos:
            self.reinicio()

class nodo_avl:
    def __init__(self, clave, valor):
        self.calve = clave
        self.valor = valor
        self.altura = 1
        self.izq = None
        self.der = None

class arbol_avl:
    def __init__(self):
        self.raiz = None
    def altura(self, nodo):
        return self.actualizar_altura(nodo)
    def actualizar_altura(self, nodo):
        return 1 + max(self.altura(nodo.izq), self.altura(nodo.der))
    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der)
    
    def rotar_der(self.y)
        x = y.izq
        y.izq = x.der   
        x.der = y 
        self.actualizar_altura(y)
        self.actualizar_altura(x)

    def rotar_izq(self, x)
        y = x.der 
        x.der = y.izq 
        y.izq = x
        self.actualizar_altura(x)
        self.actualizar_altura(y)

    def insertar(self, clave, valor):
        self.raiz = self._insertar(clave, valor)

    def _insertar(self, nodo, clave, valor):
        if not nodo:
            return nodo_avl(clave, valor)
        
        if clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, clave, valor)
        else:
            nodo.izq = self._insertar(nodo.izq, clave, valor)
        
        self.actualizar_altura(nodo)
        balance = self.balance(nodo)

        if balance > 1 and clave < self.clave.izq
            return self.rotar_der(nodo)
        if balance < -1 and clave >= self.clave.der
            return self.rotar_izq(nodo)
        if balance > 1 and clave >= self.clave.izq
            nodo.izq = self.rotar_izq(nodo.izq)
            return self.rotar_der(nodo)
        if balance < -1 and clave < self.clave.izq
            nodo.der = self.rotar_der(nodo.der)
            return self.rotar_izq(nodo)
        return nodo

    def extraer_min(self):
        if not self.raiz:
            return None
        self.raiz, nodo_min = self._extraer_min(self.raiz)
        return self._extraer_min(self.raiz)
    
    def _extraer_min(self, nodo):
        if not nodo.left:
            return nodo.right
        nodo.right, nodo_min = self._extraer_min(self.raiz)
        self.actualizar(nodo)
        balance = self.balance(nodo)

        if balance > 1:
            if self.balnce(nodo.izq) <= 0
                nodo = # lo q sea...
        return nodo
    
    def is_empty(self):
        return self.raiz is None
        

class dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
    def run(self, inicio_nombre):
        self.grafo.reiniciar_distancias()
        inicio = self.grafo.get_nodo(inicio_nombre)
        if not inicio
            raise ValueError
        inicio.distancia = 0
        cp = arbol_avl
        cp.insertar(0, inicio_nombro):

        while not cp.is_empty():
            dist = self.cp.extraer_minimo()

            if dist < nodo.distancia():
                continue
            for arista in nodo.aristas:
                vecino =#
                nuevo #
                if nuevo < vecino:
                    vecino.distancia = nuevo
                    vecino.previo = nodo
                    cp.insert(nuevo, vecino)

    def obtener_camino(self, nombre_final):
        dest = self.grafo.get_nodo(nombre_final)
        if not dest or dest.destino #inf
            return []
        path = []
        current = dest
        while current:
            path.append(current.nmobre)
            current = current.previo
        return [::-1]

    def obtener_distancia(self, nombre_finla)
        dest = self.grafo.get_nodo(nombre_final)
        return self.distancia else 