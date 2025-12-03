# =========================================================== 
#                      TDA: ARISTA 
# =========================================================== 
 
class Arista: 
    def __init__(self, origen, destino, peso): 
        self.origen = origen 
        self.destino = destino 
        self.peso = peso  # coste de pasar de origen a destino 
 
    def __repr__(self): 
        return f"{self.origen.nombre} --{self.peso}--> {self.destino.nombre}" 
 
 
# =========================================================== 
#                      TDA: GRAFO 
# =========================================================== 
 
class Grafo: 
    def __init__(self): 
        # diccionario: nombre_del_vértice -> objeto Vertice 
        self.vertices = {} 
    def agregar_vertice(self, nombre): 
        """Crea y devuelve un nuevo vértice si no existía.""" 
        if nombre not in self.vertices: 
            v = Vertice(nombre) 
            self.vertices[nombre] = v 
        return self.vertices[nombre] 
 
    def agregar_arista(self, origen_nombre, destino_nombre, peso): 
        """Crea una arista desde origen hacia destino.""" 
        origen = self.agregar_vertice(origen_nombre) 
        destino = self.agregar_vertice(destino_nombre) 
        origen.agregar_arista(destino, peso) 
 
    def obtener_vertice(self, nombre): 
        return self.vertices[nombre] 
 
    def reiniciar_distancias(self): 
        for v in self.vertices.values(): 
            v.distancia = float('inf') 
            v.anterior = None 
 
 
# =========================================================== 
#                   TDA: NODO DEL ÁRBOL AVL 
# =========================================================== 
 
class NodoAVL: 
    def __init__(self, clave, valor): 
        self.clave = clave   # distancia (prioridad) 
        self.valor = valor   # vértice asociado 
        self.altura = 1 
        self.izq = None 
        self.der = None 
 
 
# =========================================================== 
#            TDA: ÁRBOL AVL COMO COLA DE PRIORIDAD 
# =========================================================== 
 
class ArbolAVL: 
    """ 
    Árbol AVL usado como cola de prioridad para Dijkstra. 
    Métodos principales: insertar(clave, valor) y extraer_min(). 
    """ 
    def __init__(self): 
        self.raiz = None 
    # -------- utilidades -------- 
    def _altura(self, nodo): 
        return nodo.altura if nodo else 0 
 
    def _actualizar_altura(self, nodo): 
        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der)) 
 
    def _factor_equilibrio(self, nodo): 
        return self._altura(nodo.izq) - self._altura(nodo.der) 
 
    # -------- rotaciones -------- 
    def _rotar_derecha(self, y): 
        x = y.izq 
        T2 = x.der 
 
        x.der = y 
        y.izq = T2 
 
        self._actualizar_altura(y) 
        self._actualizar_altura(x) 
 
        return x 
 
    def _rotar_izquierda(self, x): 
        y = x.der 
        T2 = y.izq 
 
        y.izq = x 
        x.der = T2 
 
        self._actualizar_altura(x) 
        self._actualizar_altura(y) 
 
        return y 
 
    # -------- inserción -------- 
    def insertar(self, clave, valor): 
        self.raiz = self._insertar(self.raiz, clave, valor) 
 
    def _insertar(self, nodo, clave, valor): 
        if not nodo: 
            return NodoAVL(clave, valor) 
 
 
        if clave < nodo.clave: 
            nodo.izq = self._insertar(nodo.izq, clave, valor) 
        else: 
            nodo.der = self._insertar(nodo.der, clave, valor) 
 
        self._actualizar_altura(nodo) 
        equilibrio = self._factor_equilibrio(nodo) 
 
        # Caso Izq-Izq 
        if equilibrio > 1 and clave < nodo.izq.clave: 
            return self._rotar_derecha(nodo) 
 
        # Caso Der-Der 
        if equilibrio < -1 and clave >= nodo.der.clave: 
            return self._rotar_izquierda(nodo) 
 
        # Caso Izq-Der 
        if equilibrio > 1 and clave >= nodo.izq.clave: 
            nodo.izq = self._rotar_izquierda(nodo.izq) 
            return self._rotar_derecha(nodo) 
 
        # Caso Der-Izq 
        if equilibrio < -1 and clave < nodo.der.clave: 
            nodo.der = self._rotar_derecha(nodo.der) 
            return self._rotar_izquierda(nodo) 
 
        return nodo 
 
    # -------- extracción del mínimo -------- 
    def extraer_min(self): 
        if not self.raiz: 
            return None 
        self.raiz, min_nodo = self._extraer_min(self.raiz) 
        return min_nodo.clave, min_nodo.valor 
 
    def _extraer_min(self, nodo): 
        if nodo.izq is None: 
            return nodo.der, nodo  # reemplazamos con el hijo derecho 
 
        nodo.izq, min_nodo = self._extraer_min(nodo.izq) 
        self._actualizar_altura(nodo) 
 
        equilibrio = self._factor_equilibrio(nodo) 
 
        # reequilibrar al regresar 
        if equilibrio > 1: 
            if self._factor_equilibrio(nodo.izq) >= 0: 
                nodo = self._rotar_derecha(nodo) 
            else: 
                nodo.izq = self._rotar_izquierda(nodo.izq) 
                nodo = self._rotar_derecha(nodo) 
        elif equilibrio < -1: 
            if self._factor_equilibrio(nodo.der) <= 0: 
                nodo = self._rotar_izquierda(nodo) 
            else: 
                nodo.der = self._rotar_derecha(nodo.der) 
                nodo = self._rotar_izquierda(nodo) 
 
        return nodo, min_nodo 
 
    def esta_vacio(self): 
        return self.raiz is None 
 
 
# =========================================================== 
#                 ALGORITMO DE DIJKSTRA CON AVL 
# =========================================================== 
 
def dijkstra_con_avl(grafo, inicio_nombre): 
    grafo.reiniciar_distancias() 
 
    inicio = grafo.obtener_vertice(inicio_nombre) 
    inicio.distancia = 0 
 
    cola = ArbolAVL() 
    cola.insertar(inicio.distancia, inicio) 
 
    while not cola.esta_vacio(): 
        dist_actual, vertice_actual = cola.extraer_min() 
 
        if dist_actual > vertice_actual.distancia: 
            continue  # entrada obsoleta 
 
        # Relajación 
        for arista in vertice_actual.aristas: 
            destino = arista.destino 
            nueva_dist = vertice_actual.distancia + arista.peso 
 
            if nueva_dist < destino.distancia: 
                destino.distancia = nueva_dist 
                destino.anterior = vertice_actual 
                cola.insertar(destino.distancia, destino) 
 
 
 
 
 
 
 
 
# =========================================================== 
#          RECONSTRUIR CAMINO ÓPTIMO 
# =========================================================== 
def reconstruir_camino(grafo, inicio_nombre, fin_nombre): 
    camino = [] 
    actual = grafo.obtener_vertice(fin_nombre) 
    while actual is not None: 
        camino.append(actual.nombre) 
        actual = actual.anterior 
    camino.reverse() 
    return camino 


# ===========================================================
#  Clase Vertice mínima necesaria (se añadió para que el módulo
#  sea importable y las referencias funcionen). Si ya existe
#  otra implementación, reemplazar por la apropiada.
# ===========================================================
class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aristas = []
        self.distancia = float('inf')
        self.anterior = None

    def agregar_arista(self, destino, peso):
        self.aristas.append(Arista(self, destino, peso))

    def __repr__(self):
        return f"Vertice({self.nombre})"