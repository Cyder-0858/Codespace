"""
===================================================================================
GUÍA DE ESTUDIO PARA EXAMEN DE PYTHON - POO Y TDA
===================================================================================

TEMAS: Dijkstra + AVL + Grafos
RESTRICCIONES: Sin librerías externas, POO pura, TDA

Este archivo contiene implementaciones completas que debes estudiar y practicar.
===================================================================================
"""


# ===================================================================================
# PARTE 1: ESTRUCTURA DE DATOS - NODOS Y CLASES BÁSICAS
# ===================================================================================

class NodoArbolAVL:
    """
    Nodo para árbol AVL (Adelson-Velskii y Landis)
    Mantiene: información, altura, hijos izquierdo/derecho
    """
    def __init__(self, clave, valor=None):
        self.clave = clave          # Clave por la que se ordena
        self.valor = valor          # Valor asociado (opcional)
        self.izquierdo = None       # Hijo izquierdo
        self.derecho = None         # Hijo derecho
        self.altura = 0             # Altura del nodo
    
    def __str__(self):
        return f"Nodo({self.clave}, h={self.altura})"


class NodoGrafo:
    """
    Nodo de grafo para implementación con lista de adyacencia
    Contiene: identificador y diccionario de vecinos con pesos
    """
    def __init__(self, identificador):
        self.id = identificador
        self.adyacentes = {}  # {nodo_destino: peso}
        self.visitado = False
        self.distancia = float('inf')  # Para Dijkstra
        self.predecesor = None         # Para Dijkstra
    
    def agregar_vecino(self, vecino, peso=0):
        """Agrega una arista hacia otro nodo con su peso"""
        self.adyacentes[vecino] = peso
    
    def obtener_vecinos(self):
        """Devuelve lista de nodos vecinos"""
        return list(self.adyacentes.keys())
    
    def obtener_peso(self, vecino):
        """Obtiene el peso de la arista hacia un vecino"""
        return self.adyacentes.get(vecino, None)
    
    def __str__(self):
        return f"Nodo({self.id})"
    
    def __repr__(self):
        return self.__str__()


# ===================================================================================
# PARTE 2: ÁRBOL AVL COMPLETO
# ===================================================================================

class ArbolAVL:
    """
    Árbol Binario de Búsqueda Auto-balanceado AVL
    Operaciones principales: insertar, eliminar, buscar (todas O(log n))
    """
    def __init__(self):
        self.raiz = None
    
    # ---------------------------------------------------------------------------
    # FUNCIONES AUXILIARES DE ALTURA Y FACTOR DE EQUILIBRIO
    # ---------------------------------------------------------------------------
    
    def altura(self, nodo):
        """Devuelve la altura de un nodo (None tiene altura -1)"""
        if nodo is None:
            return -1
        return nodo.altura
    
    def actualizar_altura(self, nodo):
        """Actualiza la altura del nodo basándose en sus hijos"""
        if nodo is not None:
            altura_izq = self.altura(nodo.izquierdo)
            altura_der = self.altura(nodo.derecho)
            nodo.altura = 1 + max(altura_izq, altura_der)
    
    def factor_equilibrio(self, nodo):
        """Calcula el factor de equilibrio (altura_izq - altura_der)"""
        if nodo is None:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)
    
    # ---------------------------------------------------------------------------
    # ROTACIONES PARA BALANCEO
    # ---------------------------------------------------------------------------
    
    def rotacion_derecha(self, nodo):
        """
        Rotación simple a la derecha
                z                    y
               / \                  / \
              y   T4    -->        x   z
             / \                      / \
            x   T3                  T3  T4
        """
        nueva_raiz = nodo.izquierdo
        hijo_temp = nueva_raiz.derecho
        
        # Realizar rotación
        nueva_raiz.derecho = nodo
        nodo.izquierdo = hijo_temp
        
        # Actualizar alturas
        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)
        
        return nueva_raiz
    
    def rotacion_izquierda(self, nodo):
        """
        Rotación simple a la izquierda
            z                        y
           / \                      / \
          T1  y        -->         z   x
             / \                  / \
            T2  x                T1  T2
        """
        nueva_raiz = nodo.derecho
        hijo_temp = nueva_raiz.izquierdo
        
        # Realizar rotación
        nueva_raiz.izquierdo = nodo
        nodo.derecho = hijo_temp
        
        # Actualizar alturas
        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)
        
        return nueva_raiz
    
    def balancear(self, nodo):
        """
        Balancea el árbol si el factor de equilibrio es mayor a 1 o menor a -1
        Hay 4 casos posibles:
        1. Izquierda-Izquierda (LL): rotación derecha
        2. Derecha-Derecha (RR): rotación izquierda
        3. Izquierda-Derecha (LR): rotación izq + rotación der
        4. Derecha-Izquierda (RL): rotación der + rotación izq
        """
        if nodo is None:
            return nodo
        
        # Actualizar altura del nodo actual
        self.actualizar_altura(nodo)
        
        # Obtener factor de equilibrio
        balance = self.factor_equilibrio(nodo)
        
        # Caso 1: Izquierda-Izquierda (LL)
        if balance > 1 and self.factor_equilibrio(nodo.izquierdo) >= 0:
            return self.rotacion_derecha(nodo)
        
        # Caso 2: Derecha-Derecha (RR)
        if balance < -1 and self.factor_equilibrio(nodo.derecho) <= 0:
            return self.rotacion_izquierda(nodo)
        
        # Caso 3: Izquierda-Derecha (LR)
        if balance > 1 and self.factor_equilibrio(nodo.izquierdo) < 0:
            nodo.izquierdo = self.rotacion_izquierda(nodo.izquierdo)
            return self.rotacion_derecha(nodo)
        
        # Caso 4: Derecha-Izquierda (RL)
        if balance < -1 and self.factor_equilibrio(nodo.derecho) > 0:
            nodo.derecho = self.rotacion_derecha(nodo.derecho)
            return self.rotacion_izquierda(nodo)
        
        return nodo
    
    # ---------------------------------------------------------------------------
    # OPERACIONES PRINCIPALES
    # ---------------------------------------------------------------------------
    
    def insertar(self, clave, valor=None):
        """Inserta un elemento en el árbol AVL"""
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)
    
    def _insertar_recursivo(self, nodo, clave, valor):
        """Función recursiva auxiliar para insertar"""
        # Caso base: posición encontrada
        if nodo is None:
            return NodoArbolAVL(clave, valor)
        
        # Inserción recursiva normal de BST
        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            # Clave duplicada - actualizar valor
            nodo.valor = valor
            return nodo
        
        # Balancear el árbol después de insertar
        return self.balancear(nodo)
    
    def buscar(self, clave):
        """Busca un nodo por su clave"""
        return self._buscar_recursivo(self.raiz, clave)
    
    def _buscar_recursivo(self, nodo, clave):
        """Función recursiva auxiliar para buscar"""
        if nodo is None:
            return None
        
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        else:
            return self._buscar_recursivo(nodo.derecho, clave)
    
    def eliminar(self, clave):
        """Elimina un nodo del árbol AVL"""
        self.raiz = self._eliminar_recursivo(self.raiz, clave)
    
    def _eliminar_recursivo(self, nodo, clave):
        """Función recursiva auxiliar para eliminar"""
        if nodo is None:
            return None
        
        # Buscar el nodo a eliminar
        if clave < nodo.clave:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, clave)
        else:
            # Nodo encontrado - eliminar
            # Caso 1: Nodo hoja o con un hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            
            # Caso 2: Nodo con dos hijos
            # Encontrar el sucesor in-order (menor del subárbol derecho)
            sucesor = self._minimo_nodo(nodo.derecho)
            nodo.clave = sucesor.clave
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.clave)
        
        # Balancear el árbol después de eliminar
        return self.balancear(nodo)
    
    def _minimo_nodo(self, nodo):
        """Encuentra el nodo con la clave mínima en un subárbol"""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    # ---------------------------------------------------------------------------
    # RECORRIDOS
    # ---------------------------------------------------------------------------
    
    def inorden(self):
        """Recorrido in-orden (izquierda-raíz-derecha) - devuelve lista ordenada"""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append((nodo.clave, nodo.valor))
            self._inorden_recursivo(nodo.derecho, resultado)
    
    def preorden(self):
        """Recorrido pre-orden (raíz-izquierda-derecha)"""
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _preorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append((nodo.clave, nodo.valor))
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)
    
    def postorden(self):
        """Recorrido post-orden (izquierda-derecha-raíz)"""
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _postorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierdo, resultado)
            self._postorden_recursivo(nodo.derecho, resultado)
            resultado.append((nodo.clave, nodo.valor))
    
    def arbol_vacio(self):
        """Verifica si el árbol está vacío"""
        return self.raiz is None


# ===================================================================================
# PARTE 3: GRAFO CON LISTA DE ADYACENCIA
# ===================================================================================

class Grafo:
    """
    Grafo implementado con lista de adyacencia
    Puede ser dirigido o no dirigido
    """
    def __init__(self, dirigido=True):
        self.nodos = {}  # {id: NodoGrafo}
        self.dirigido = dirigido
    
    def agregar_nodo(self, identificador):
        """Agrega un nodo al grafo"""
        if identificador not in self.nodos:
            self.nodos[identificador] = NodoGrafo(identificador)
    
    def agregar_arista(self, origen, destino, peso=1):
        """Agrega una arista entre dos nodos"""
        # Asegurar que ambos nodos existen
        if origen not in self.nodos:
            self.agregar_nodo(origen)
        if destino not in self.nodos:
            self.agregar_nodo(destino)
        
        # Agregar arista
        self.nodos[origen].agregar_vecino(self.nodos[destino], peso)
        
        # Si no es dirigido, agregar arista inversa
        if not self.dirigido:
            self.nodos[destino].agregar_vecino(self.nodos[origen], peso)
    
    def obtener_nodo(self, identificador):
        """Obtiene un nodo por su identificador"""
        return self.nodos.get(identificador, None)
    
    def obtener_nodos(self):
        """Devuelve lista de todos los nodos"""
        return list(self.nodos.values())
    
    def reiniciar_nodos(self):
        """Reinicia atributos de búsqueda de todos los nodos"""
        for nodo in self.nodos.values():
            nodo.visitado = False
            nodo.distancia = float('inf')
            nodo.predecesor = None
    
    def __str__(self):
        resultado = "Grafo:\n"
        for id_nodo, nodo in self.nodos.items():
            adyacentes = [(v.id, peso) for v, peso in nodo.adyacentes.items()]
            resultado += f"  {id_nodo} -> {adyacentes}\n"
        return resultado


# ===================================================================================
# PARTE 4: COLA DE PRIORIDAD CON MONTÍCULO MÍNIMO (HEAP)
# ===================================================================================

class ColaPrioridad:
    """
    Cola de prioridad implementada con montículo mínimo (min-heap)
    Esencial para Dijkstra eficiente
    """
    def __init__(self):
        self.heap = []  # Lista que representa el heap
        self.indice_mapa = {}  # {nodo: índice} para operaciones O(log n)
    
    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        return len(self.heap) == 0
    
    def insertar(self, nodo, prioridad):
        """Inserta un elemento con su prioridad"""
        # Agregar al final
        self.heap.append((prioridad, nodo))
        indice = len(self.heap) - 1
        self.indice_mapa[nodo] = indice
        
        # Flotar hacia arriba
        self._flotar(indice)
    
    def extraer_minimo(self):
        """Extrae y devuelve el elemento con menor prioridad"""
        if self.esta_vacia():
            return None
        
        # Guardar el mínimo
        minimo = self.heap[0]
        
        # Mover el último al principio
        ultimo = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = ultimo
            self.indice_mapa[ultimo[1]] = 0
            # Hundir hacia abajo
            self._hundir(0)
        
        # Limpiar del mapa
        del self.indice_mapa[minimo[1]]
        
        return minimo[1]
    
    def disminuir_prioridad(self, nodo, nueva_prioridad):
        """Disminuye la prioridad de un nodo existente"""
        if nodo not in self.indice_mapa:
            return
        
        indice = self.indice_mapa[nodo]
        self.heap[indice] = (nueva_prioridad, nodo)
        self._flotar(indice)
    
    def contiene(self, nodo):
        """Verifica si un nodo está en la cola"""
        return nodo in self.indice_mapa
    
    def _flotar(self, indice):
        """Flota un elemento hacia arriba hasta su posición correcta"""
        while indice > 0:
            padre = (indice - 1) // 2
            if self.heap[indice][0] < self.heap[padre][0]:
                # Intercambiar
                self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
                self.indice_mapa[self.heap[indice][1]] = indice
                self.indice_mapa[self.heap[padre][1]] = padre
                indice = padre
            else:
                break
    
    def _hundir(self, indice):
        """Hunde un elemento hacia abajo hasta su posición correcta"""
        tamanio = len(self.heap)
        while True:
            hijo_izq = 2 * indice + 1
            hijo_der = 2 * indice + 2
            minimo = indice
            
            # Comparar con hijo izquierdo
            if hijo_izq < tamanio and self.heap[hijo_izq][0] < self.heap[minimo][0]:
                minimo = hijo_izq
            
            # Comparar con hijo derecho
            if hijo_der < tamanio and self.heap[hijo_der][0] < self.heap[minimo][0]:
                minimo = hijo_der
            
            # Si no hay cambio, terminar
            if minimo == indice:
                break
            
            # Intercambiar
            self.heap[indice], self.heap[minimo] = self.heap[minimo], self.heap[indice]
            self.indice_mapa[self.heap[indice][1]] = indice
            self.indice_mapa[self.heap[minimo][1]] = minimo
            indice = minimo


# ===================================================================================
# PARTE 5: ALGORITMO DE DIJKSTRA
# ===================================================================================

class Dijkstra:
    """
    Implementación del algoritmo de Dijkstra para caminos más cortos
    desde un nodo origen a todos los demás nodos
    """
    def __init__(self, grafo):
        self.grafo = grafo
        self.caminos = {}  # {nodo_id: (distancia, camino)}
    
    def ejecutar(self, origen_id):
        """
        Ejecuta Dijkstra desde el nodo origen
        Devuelve diccionario de distancias y predecesores
        """
        # Reiniciar nodos
        self.grafo.reiniciar_nodos()
        
        # Verificar que el origen existe
        if origen_id not in self.grafo.nodos:
            print(f"Error: Nodo {origen_id} no existe en el grafo")
            return None
        
        nodo_origen = self.grafo.obtener_nodo(origen_id)
        nodo_origen.distancia = 0
        
        # Cola de prioridad para procesar nodos
        cola = ColaPrioridad()
        cola.insertar(nodo_origen, 0)
        
        # Procesar mientras haya nodos
        while not cola.esta_vacia():
            # Extraer nodo con menor distancia
            nodo_actual = cola.extraer_minimo()
            
            # Marcar como visitado
            nodo_actual.visitado = True
            
            # Explorar vecinos
            for vecino in nodo_actual.obtener_vecinos():
                if not vecino.visitado:
                    # Calcular nueva distancia
                    peso_arista = nodo_actual.obtener_peso(vecino)
                    nueva_distancia = nodo_actual.distancia + peso_arista
                    
                    # Si encontramos un camino más corto
                    if nueva_distancia < vecino.distancia:
                        vecino.distancia = nueva_distancia
                        vecino.predecesor = nodo_actual
                        
                        # Actualizar en la cola de prioridad
                        if cola.contiene(vecino):
                            cola.disminuir_prioridad(vecino, nueva_distancia)
                        else:
                            cola.insertar(vecino, nueva_distancia)
        
        # Construir tabla de resultados
        self._construir_caminos()
        return self.caminos
    
    def _construir_caminos(self):
        """Construye los caminos desde origen a cada nodo"""
        self.caminos = {}
        for nodo_id, nodo in self.grafo.nodos.items():
            camino = self._reconstruir_camino(nodo)
            self.caminos[nodo_id] = {
                'distancia': nodo.distancia,
                'camino': camino
            }
    
    def _reconstruir_camino(self, nodo_destino):
        """Reconstruye el camino desde origen hasta destino"""
        if nodo_destino.distancia == float('inf'):
            return None  # No hay camino
        
        camino = []
        actual = nodo_destino
        
        while actual is not None:
            camino.insert(0, actual.id)
            actual = actual.predecesor
        
        return camino
    
    def obtener_camino(self, destino_id):
        """Obtiene el camino más corto hacia un destino específico"""
        if destino_id in self.caminos:
            return self.caminos[destino_id]
        return None
    
    def imprimir_resultados(self):
        """Imprime todos los caminos y distancias"""
        print("\n" + "="*60)
        print("RESULTADOS DE DIJKSTRA")
        print("="*60)
        
        for nodo_id in sorted(self.caminos.keys()):
            info = self.caminos[nodo_id]
            distancia = info['distancia']
            camino = info['camino']
            
            if distancia == float('inf'):
                print(f"{nodo_id}: No alcanzable")
            else:
                camino_str = " -> ".join(str(n) for n in camino)
                print(f"{nodo_id}: Distancia = {distancia}, Camino = {camino_str}")


# ===================================================================================
# PARTE 6: DIJKSTRA CON AVL (VERSIÓN OPTIMIZADA)
# ===================================================================================

class DijkstraConAVL:
    """
    Implementación de Dijkstra usando AVL en lugar de heap
    El AVL mantiene los nodos ordenados por distancia
    """
    def __init__(self, grafo):
        self.grafo = grafo
        self.caminos = {}
        self.avl = None  # Árbol AVL para mantener nodos por distancia
    
    def ejecutar(self, origen_id):
        """Ejecuta Dijkstra usando AVL como estructura de prioridad"""
        # Reiniciar
        self.grafo.reiniciar_nodos()
        self.avl = ArbolAVL()
        
        if origen_id not in self.grafo.nodos:
            print(f"Error: Nodo {origen_id} no existe")
            return None
        
        nodo_origen = self.grafo.obtener_nodo(origen_id)
        nodo_origen.distancia = 0
        
        # Insertar todos los nodos en el AVL (clave = distancia, valor = nodo)
        for nodo in self.grafo.obtener_nodos():
            # Usar tupla (distancia, id) como clave para mantener unicidad
            clave = (nodo.distancia, nodo.id)
            self.avl.insertar(clave, nodo)
        
        # Procesar nodos
        while not self.avl.arbol_vacio():
            # Extraer nodo con menor distancia (más a la izquierda)
            nodo_actual = self._extraer_minimo()
            
            if nodo_actual is None or nodo_actual.distancia == float('inf'):
                break
            
            nodo_actual.visitado = True
            
            # Explorar vecinos
            for vecino in nodo_actual.obtener_vecinos():
                if not vecino.visitado:
                    peso_arista = nodo_actual.obtener_peso(vecino)
                    nueva_distancia = nodo_actual.distancia + peso_arista
                    
                    if nueva_distancia < vecino.distancia:
                        # Eliminar del AVL con distancia antigua
                        clave_antigua = (vecino.distancia, vecino.id)
                        self.avl.eliminar(clave_antigua)
                        
                        # Actualizar distancia
                        vecino.distancia = nueva_distancia
                        vecino.predecesor = nodo_actual
                        
                        # Reinsertar con nueva distancia
                        clave_nueva = (vecino.distancia, vecino.id)
                        self.avl.insertar(clave_nueva, vecino)
        
        # Construir resultados
        self._construir_caminos()
        return self.caminos
    
    def _extraer_minimo(self):
        """Extrae el nodo con menor distancia del AVL"""
        if self.avl.arbol_vacio():
            return None
        
        # Encontrar el nodo más a la izquierda (menor clave)
        nodo_min = self.avl.raiz
        while nodo_min.izquierdo is not None:
            nodo_min = nodo_min.izquierdo
        
        # Extraer el valor (nodo del grafo)
        nodo_grafo = nodo_min.valor
        
        # Eliminar del AVL
        self.avl.eliminar(nodo_min.clave)
        
        return nodo_grafo
    
    def _construir_caminos(self):
        """Construye la tabla de caminos"""
        self.caminos = {}
        for nodo_id, nodo in self.grafo.nodos.items():
            camino = self._reconstruir_camino(nodo)
            self.caminos[nodo_id] = {
                'distancia': nodo.distancia,
                'camino': camino
            }
    
    def _reconstruir_camino(self, nodo_destino):
        """Reconstruye el camino desde origen"""
        if nodo_destino.distancia == float('inf'):
            return None
        
        camino = []
        actual = nodo_destino
        
        while actual is not None:
            camino.insert(0, actual.id)
            actual = actual.predecesor
        
        return camino
    
    def imprimir_resultados(self):
        """Imprime los resultados"""
        print("\n" + "="*60)
        print("RESULTADOS DE DIJKSTRA CON AVL")
        print("="*60)
        
        for nodo_id in sorted(self.caminos.keys()):
            info = self.caminos[nodo_id]
            distancia = info['distancia']
            camino = info['camino']
            
            if distancia == float('inf'):
                print(f"{nodo_id}: No alcanzable")
            else:
                camino_str = " -> ".join(str(n) for n in camino)
                print(f"{nodo_id}: Distancia = {distancia}, Camino = {camino_str}")


# ===================================================================================
# PARTE 7: EJEMPLOS Y PRUEBAS
# ===================================================================================

def ejemplo_avl():
    """Ejemplo de uso del árbol AVL"""
    print("\n" + "="*60)
    print("EJEMPLO: ÁRBOL AVL")
    print("="*60)
    
    avl = ArbolAVL()
    
    # Insertar elementos
    elementos = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35]
    print(f"\nInsertando elementos: {elementos}")
    
    for elem in elementos:
        avl.insertar(elem)
    
    # Recorridos
    print("\nRecorrido Inorden (ordenado):")
    print([k for k, v in avl.inorden()])
    
    print("\nRecorrido Preorden:")
    print([k for k, v in avl.preorden()])
    
    # Buscar
    print("\nBuscar elemento 27:")
    nodo = avl.buscar(27)
    print(f"Encontrado: {nodo is not None}")
    
    # Eliminar
    print("\nEliminar elemento 25:")
    avl.eliminar(25)
    print("Inorden después de eliminar:")
    print([k for k, v in avl.inorden()])


def ejemplo_grafo_dijkstra():
    """Ejemplo de Dijkstra con grafo"""
    print("\n" + "="*60)
    print("EJEMPLO: DIJKSTRA CON GRAFO")
    print("="*60)
    
    # Crear grafo
    grafo = Grafo(dirigido=True)
    
    # Agregar aristas (grafo del ejemplo típico)
    aristas = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    
    for origen, destino, peso in aristas:
        grafo.agregar_arista(origen, destino, peso)
    
    print("\nGrafo creado:")
    print(grafo)
    
    # Ejecutar Dijkstra
    dijkstra = Dijkstra(grafo)
    dijkstra.ejecutar('A')
    dijkstra.imprimir_resultados()
    
    # Obtener camino específico
    print("\nCamino más corto de A a F:")
    info = dijkstra.obtener_camino('F')
    if info:
        print(f"Distancia: {info['distancia']}")
        print(f"Camino: {' -> '.join(info['camino'])}")


def ejemplo_dijkstra_con_avl():
    """Ejemplo de Dijkstra usando AVL"""
    print("\n" + "="*60)
    print("EJEMPLO: DIJKSTRA CON AVL")
    print("="*60)
    
    # Crear mismo grafo
    grafo = Grafo(dirigido=True)
    
    aristas = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    
    for origen, destino, peso in aristas:
        grafo.agregar_arista(origen, destino, peso)
    
    print("\nGrafo creado (mismo del ejemplo anterior)")
    
    # Ejecutar Dijkstra con AVL
    dijkstra_avl = DijkstraConAVL(grafo)
    dijkstra_avl.ejecutar('A')
    dijkstra_avl.imprimir_resultados()


# ===================================================================================
# MAIN - EJECUTAR TODOS LOS EJEMPLOS
# ===================================================================================

if __name__ == "__main__":
    print("\n")
    print("#" * 70)
    print("#" + " " * 68 + "#")
    print("#" + "  GUÍA COMPLETA: DIJKSTRA + AVL + GRAFOS (POO PURO)".center(68) + "#")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    
    # Ejecutar ejemplos
    ejemplo_avl()
    ejemplo_grafo_dijkstra()
    ejemplo_dijkstra_con_avl()
    
    print("\n" + "="*60)
    print("FIN DE LOS EJEMPLOS")
    print("="*60)
    print("\n¡Estudia cada implementación y practica modificándolas!")
    print("Recuerda: TODO debe ser POO puro, sin librerías externas.\n")
