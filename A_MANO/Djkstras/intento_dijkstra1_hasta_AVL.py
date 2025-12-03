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
        self.raiz = None

    def altura(self, nodo):
        return nodo.altura if nodo else 0
    
    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0
    
    def rotar_derecha(self, y):
        x = y.izq
        y.izq = x.der
        x.der = y
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return x
    
    def rotar_izquierda(self, x):
        y = x.der
        x.der = y.izq
        y.izq = x
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        return y
    
    def insertar(self, clave, valor):
        self.raiz = self._insertar(self.raiz, clave, valor)

    def _insertar(self, nodo, clave, valor):
        if not nodo:
            return nodo_avl(clave, valor)
        if clave > nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave, valor)
        else:
            nodo.der = self._insertar(nodo.der, clave, valor)

        self.actualizar_altura(nodo)
        balance = self.balance(nodo)

        if balance > 1 and clave < nodo.izq.clave:
            return self.rotar_derecha(nodo)
        if balance < -1 and clave > nodo.der.clave:
            return self.rotar_izquierda(nodo)
        if balance > 1 and clave > nodo.izq.clave:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)
        if balance < -1 and clave < nodo.der.clave:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)
        return nodo
    
    def extraer_minimo(self):
        if not self.raiz:
            return Nones
        self.raiz, nodo_minimo = self._extraer_minimo(self.raiz)
        return nodo_minimo
    
    def _extraer_minimo(self, nodo):
        if nodo.izq is None:
            return nodo.der, nodo
        nodo.izq, nodo_minimo = self._extraer_minimo(nodo.izq)
        self.actualizar_altura(nodo)
        balance = self.balance(nodo)

        if balance > 1 and self.balance(nodo.izq) >= 0:
            return self.rotar_derecha(nodo), nodo_minimo
        if balance < -1 and self.balance(nodo.der) <= 0:
            return self.rotar_izquierda(nodo), nodo_minimo
        if balance > 1 and self.balance(nodo.izq) < 0:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo), nodo_minimo
        if balance < -1 and self.balance(nodo.der) > 0:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo), nodo_minimo
        return nodo, nodo_minimo
    
    def es_vacio(self):
        return self.raiz is None
    

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def recorrer(self, nodo_inicio):
        self.grafo.reiniciar_distancias()
        inicio = self.grafo.get_nodo(nodo_inicio)
        if not inicio:
            return 0

        inicio.distancia = 0
        cola_prioridad = arbol_avl()
        cola_prioridad(0, inicio)

        while not cola_prioridad.es_vacio():
            dist, nodo = cola_prioridad.extraer_minimo()

            if dist > vecino.distancia;
                vecino.distancia = nueva_dist
                vecino.previo = nodo
                cola_prioridad.insertar(nueva_dist, vecino)
    
    def obtener_camino(self, nombre_destino):
        if not dest or dest.distancia == float("inf"):
            return []
        
        path = []
        actual = dest
        while actual:
            path.append(actual.nombre)
            actual = actual.nodo_anterior

        return path[::-1]
    
    def obtener_distancia(self, nombre_destino):
        nodo = self.grafo.get_nodo(nombre_destino)
        return nodo.distancia if nodo else float("inf")
    