"""
===================================================================================
EJERCICIO RESUELTO PASO A PASO - TIPO EXAMEN
===================================================================================

ENUNCIADO:
----------
Se tiene una red de distribución de paquetes entre almacenes. Cada almacén está
conectado con otros mediante rutas con diferentes distancias en kilómetros.

Se pide implementar:
1. Un sistema de grafo dirigido para representar la red de almacenes
2. Un árbol AVL para optimizar las búsquedas en Dijkstra
3. El algoritmo de Dijkstra para encontrar rutas más cortas
4. Todo debe ser POO puro, sin usar librerías externas

Datos de la red:
- Almacenes: A, B, C, D, E, F
- Rutas (origen -> destino: distancia_km):
  * A -> B: 7
  * A -> C: 9
  * A -> F: 14
  * B -> C: 10
  * B -> D: 15
  * C -> D: 11
  * C -> F: 2
  * D -> E: 6
  * E -> F: 9
  
Tarea: Encontrar las rutas más cortas desde el almacén A hacia todos los demás.

===================================================================================
"""


# ===================================================================================
# PASO 1: DEFINIR LAS ESTRUCTURAS DE NODOS
# ===================================================================================
"""
RAZONAMIENTO:
Necesitamos dos tipos de nodos:
1. NodoAVL: para el árbol AVL que usaremos como cola de prioridad
2. NodoGrafo: para representar los almacenes y sus conexiones

¿Por qué separar los nodos?
- Cada uno tiene propósitos diferentes
- NodoAVL: almacenar datos ordenados por clave
- NodoGrafo: almacenar información de red (vecinos, distancias)
"""

class NodoAVL:
    """
    Nodo del árbol AVL
    
    Atributos:
    - clave: valor por el que se ordena el árbol (tuple: distancia, id)
    - valor: objeto NodoGrafo asociado
    - izquierdo, derecho: hijos del nodo
    - altura: altura del subárbol con raíz en este nodo
    """
    def __init__(self, clave, valor=None):
        self.clave = clave          # (distancia, id_almacen) para ordenar
        self.valor = valor          # NodoGrafo correspondiente
        self.izquierdo = None       # Hijo izquierdo
        self.derecho = None         # Hijo derecho
        self.altura = 0             # Altura para balanceo
    
    def __str__(self):
        return f"AVL[{self.clave}]"


class NodoGrafo:
    """
    Nodo del grafo que representa un almacén
    
    Atributos:
    - id: identificador del almacén (ej: 'A', 'B', etc.)
    - adyacentes: diccionario {NodoGrafo_destino: distancia}
    - distancia: distancia mínima desde origen (para Dijkstra)
    - predecesor: nodo previo en el camino más corto (para Dijkstra)
    - visitado: marca si ya fue procesado (para Dijkstra)
    """
    def __init__(self, identificador):
        self.id = identificador
        self.adyacentes = {}        # {NodoGrafo: distancia_km}
        self.distancia = float('inf')  # Inicialmente: distancia infinita
        self.predecesor = None      # Inicialmente: sin predecesor
        self.visitado = False       # Inicialmente: no visitado
    
    def agregar_ruta(self, destino, distancia_km):
        """Agrega una ruta desde este almacén hacia otro"""
        self.adyacentes[destino] = distancia_km
    
    def obtener_rutas(self):
        """Devuelve lista de almacenes conectados"""
        return list(self.adyacentes.keys())
    
    def obtener_distancia_a(self, destino):
        """Obtiene la distancia a un almacén vecino"""
        return self.adyacentes.get(destino, None)
    
    def __str__(self):
        return f"Almacén({self.id})"
    
    def __repr__(self):
        return self.__str__()


# ===================================================================================
# PASO 2: IMPLEMENTAR EL ÁRBOL AVL
# ===================================================================================
"""
RAZONAMIENTO:
El AVL nos permite mantener nodos ordenados por distancia con operaciones O(log n).
Esto es crucial para Dijkstra, donde constantemente necesitamos el nodo con menor
distancia.

Operaciones clave:
- altura(): calcular altura de un nodo
- factor_equilibrio(): determinar si está balanceado
- rotaciones: simple_derecha, simple_izquierda
- balancear(): aplicar rotaciones según sea necesario
- insertar(): agregar nodo manteniendo balance
- eliminar(): quitar nodo manteniendo balance
"""

class ArbolAVL:
    """
    Árbol Binario de Búsqueda Auto-balanceado AVL
    Mantiene operaciones O(log n) mediante rotaciones
    """
    def __init__(self):
        self.raiz = None
    
    # -------- FUNCIONES AUXILIARES --------
    
    def altura(self, nodo):
        """
        Devuelve la altura de un nodo.
        Nodo None tiene altura -1 por convención.
        """
        if nodo is None:
            return -1
        return nodo.altura
    
    def actualizar_altura(self, nodo):
        """
        Actualiza la altura de un nodo basándose en sus hijos.
        altura = 1 + max(altura_hijo_izq, altura_hijo_der)
        """
        if nodo is not None:
            alt_izq = self.altura(nodo.izquierdo)
            alt_der = self.altura(nodo.derecho)
            nodo.altura = 1 + max(alt_izq, alt_der)
    
    def factor_equilibrio(self, nodo):
        """
        Calcula el factor de equilibrio.
        FE = altura(subárbol_izq) - altura(subárbol_der)
        
        Si |FE| > 1, el árbol está desbalanceado.
        """
        if nodo is None:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)
    
    # -------- ROTACIONES --------
    
    def rotacion_derecha(self, z):
        """
        Rotación simple a la derecha
        
        Antes:           Después:
            z               y
           / \             / \
          y   T4   -->    x   z
         / \                 / \
        x   T3             T3  T4
        
        Casos de uso: LL (Left-Left)
        """
        y = z.izquierdo
        T3 = y.derecho
        
        # Realizar rotación
        y.derecho = z
        z.izquierdo = T3
        
        # Actualizar alturas (primero z, luego y)
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        
        return y  # Nueva raíz del subárbol
    
    def rotacion_izquierda(self, z):
        """
        Rotación simple a la izquierda
        
        Antes:           Después:
          z                 y
         / \               / \
        T1  y     -->     z   x
           / \           / \
          T2  x        T1  T2
        
        Casos de uso: RR (Right-Right)
        """
        y = z.derecho
        T2 = y.izquierdo
        
        # Realizar rotación
        y.izquierdo = z
        z.derecho = T2
        
        # Actualizar alturas
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        
        return y  # Nueva raíz del subárbol
    
    # -------- BALANCEO --------
    
    def balancear(self, nodo):
        """
        Balancea el nodo si es necesario.
        
        Hay 4 casos posibles:
        1. LL (Left-Left): balance > 1 y hijo_izq.balance >= 0
           Solución: rotación simple derecha
        
        2. RR (Right-Right): balance < -1 y hijo_der.balance <= 0
           Solución: rotación simple izquierda
        
        3. LR (Left-Right): balance > 1 y hijo_izq.balance < 0
           Solución: rotación izq en hijo_izq, luego rotación der en nodo
        
        4. RL (Right-Left): balance < -1 y hijo_der.balance > 0
           Solución: rotación der en hijo_der, luego rotación izq en nodo
        """
        if nodo is None:
            return nodo
        
        # Actualizar altura
        self.actualizar_altura(nodo)
        
        # Calcular factor de equilibrio
        balance = self.factor_equilibrio(nodo)
        
        # Caso 1: LL (Left-Left)
        if balance > 1 and self.factor_equilibrio(nodo.izquierdo) >= 0:
            print(f"  [Balanceo] Caso LL en {nodo.clave}")
            return self.rotacion_derecha(nodo)
        
        # Caso 2: RR (Right-Right)
        if balance < -1 and self.factor_equilibrio(nodo.derecho) <= 0:
            print(f"  [Balanceo] Caso RR en {nodo.clave}")
            return self.rotacion_izquierda(nodo)
        
        # Caso 3: LR (Left-Right)
        if balance > 1 and self.factor_equilibrio(nodo.izquierdo) < 0:
            print(f"  [Balanceo] Caso LR en {nodo.clave}")
            nodo.izquierdo = self.rotacion_izquierda(nodo.izquierdo)
            return self.rotacion_derecha(nodo)
        
        # Caso 4: RL (Right-Left)
        if balance < -1 and self.factor_equilibrio(nodo.derecho) > 0:
            print(f"  [Balanceo] Caso RL en {nodo.clave}")
            nodo.derecho = self.rotacion_derecha(nodo.derecho)
            return self.rotacion_izquierda(nodo)
        
        # No necesita balanceo
        return nodo
    
    # -------- OPERACIONES PRINCIPALES --------
    
    def insertar(self, clave, valor=None):
        """Inserta un elemento en el AVL manteniendo balance"""
        print(f"  [AVL] Insertando {clave}")
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)
    
    def _insertar_recursivo(self, nodo, clave, valor):
        """Función recursiva auxiliar para insertar"""
        # Caso base: posición encontrada
        if nodo is None:
            return NodoAVL(clave, valor)
        
        # Inserción BST estándar
        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            # Clave duplicada: actualizar valor
            nodo.valor = valor
            return nodo
        
        # Balancear después de insertar
        return self.balancear(nodo)
    
    def eliminar(self, clave):
        """Elimina un elemento del AVL manteniendo balance"""
        print(f"  [AVL] Eliminando {clave}")
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
            # Nodo encontrado
            # Caso 1 y 2: nodo con 0 o 1 hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            
            # Caso 3: nodo con 2 hijos
            # Encontrar sucesor (mínimo del subárbol derecho)
            sucesor = self._minimo_nodo(nodo.derecho)
            nodo.clave = sucesor.clave
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.clave)
        
        # Balancear después de eliminar
        return self.balancear(nodo)
    
    def _minimo_nodo(self, nodo):
        """Encuentra el nodo con la clave mínima"""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
    
    def arbol_vacio(self):
        """Verifica si el árbol está vacío"""
        return self.raiz is None
    
    def extraer_minimo(self):
        """
        Extrae y devuelve el elemento con menor clave.
        Esta es una operación clave para Dijkstra.
        """
        if self.arbol_vacio():
            return None
        
        # Encontrar el nodo más a la izquierda
        nodo_min = self.raiz
        while nodo_min.izquierdo is not None:
            nodo_min = nodo_min.izquierdo
        
        # Guardar valor antes de eliminar
        valor = nodo_min.valor
        clave = nodo_min.clave
        
        # Eliminar ese nodo
        self.eliminar(clave)
        
        return valor


# ===================================================================================
# PASO 3: IMPLEMENTAR EL GRAFO
# ===================================================================================
"""
RAZONAMIENTO:
El grafo representa nuestra red de almacenes.
Usamos lista de adyacencia porque es más eficiente que matriz para grafos dispersos.
"""

class Grafo:
    """
    Grafo dirigido con lista de adyacencia
    Representa la red de almacenes y rutas
    """
    def __init__(self):
        self.nodos = {}  # {id_almacen: NodoGrafo}
    
    def agregar_almacen(self, identificador):
        """Agrega un almacén a la red"""
        if identificador not in self.nodos:
            self.nodos[identificador] = NodoGrafo(identificador)
            print(f"[Grafo] Almacén {identificador} agregado")
    
    def agregar_ruta(self, origen, destino, distancia):
        """
        Agrega una ruta dirigida entre dos almacenes.
        Si los almacenes no existen, los crea automáticamente.
        """
        # Asegurar que ambos almacenes existen
        if origen not in self.nodos:
            self.agregar_almacen(origen)
        if destino not in self.nodos:
            self.agregar_almacen(destino)
        
        # Agregar la ruta
        self.nodos[origen].agregar_ruta(self.nodos[destino], distancia)
        print(f"[Grafo] Ruta {origen} -> {destino}: {distancia} km")
    
    def obtener_almacen(self, identificador):
        """Obtiene un almacén por su identificador"""
        return self.nodos.get(identificador, None)
    
    def obtener_todos_almacenes(self):
        """Devuelve lista de todos los almacenes"""
        return list(self.nodos.values())
    
    def reiniciar_para_dijkstra(self):
        """Reinicia todos los almacenes para una nueva ejecución de Dijkstra"""
        print("[Grafo] Reiniciando almacenes para Dijkstra...")
        for almacen in self.nodos.values():
            almacen.visitado = False
            almacen.distancia = float('inf')
            almacen.predecesor = None
    
    def __str__(self):
        resultado = "\n=== RED DE ALMACENES ===\n"
        for id_almacen in sorted(self.nodos.keys()):
            almacen = self.nodos[id_almacen]
            rutas = [(dest.id, dist) for dest, dist in almacen.adyacentes.items()]
            resultado += f"{id_almacen} -> {rutas}\n"
        return resultado


# ===================================================================================
# PASO 4: IMPLEMENTAR DIJKSTRA CON AVL
# ===================================================================================
"""
RAZONAMIENTO:
Dijkstra encuentra el camino más corto desde un origen a todos los demás nodos.
Usamos el AVL como cola de prioridad para extraer eficientemente el nodo con
menor distancia en cada iteración.

Complejidad: O((V + E) log V) donde V = vértices, E = aristas
"""

class DijkstraConAVL:
    """
    Implementación del algoritmo de Dijkstra usando AVL
    para encontrar caminos más cortos
    """
    def __init__(self, grafo):
        self.grafo = grafo
        self.resultados = {}  # {id_almacen: {'distancia': X, 'camino': [...]}}
    
    def ejecutar(self, origen_id):
        """
        Ejecuta Dijkstra desde el almacén origen.
        
        Algoritmo:
        1. Inicializar: distancia[origen] = 0, resto = infinito
        2. Insertar todos los nodos en AVL ordenados por distancia
        3. Mientras AVL no vacío:
           a) Extraer nodo con menor distancia
           b) Marcar como visitado
           c) Para cada vecino no visitado:
              - Calcular nueva distancia
              - Si es menor, actualizar y reinsertar en AVL
        4. Reconstruir caminos usando predecesores
        """
        print("\n" + "="*70)
        print(f"EJECUTANDO DIJKSTRA DESDE ALMACÉN {origen_id}")
        print("="*70)
        
        # Paso 1: Inicializar
        self.grafo.reiniciar_para_dijkstra()
        
        if origen_id not in self.grafo.nodos:
            print(f"ERROR: Almacén {origen_id} no existe")
            return None
        
        almacen_origen = self.grafo.obtener_almacen(origen_id)
        almacen_origen.distancia = 0
        
        # Paso 2: Crear AVL con todos los almacenes
        print("\n[Dijkstra] Inicializando AVL con todos los almacenes...")
        avl = ArbolAVL()
        
        for almacen in self.grafo.obtener_todos_almacenes():
            # Clave = (distancia, id) para mantener orden y unicidad
            clave = (almacen.distancia, almacen.id)
            avl.insertar(clave, almacen)
        
        print(f"[Dijkstra] AVL inicializado con {len(self.grafo.nodos)} almacenes")
        
        # Paso 3: Procesar almacenes
        print("\n[Dijkstra] Procesando almacenes...\n")
        iteracion = 0
        
        while not avl.arbol_vacio():
            iteracion += 1
            print(f"--- Iteración {iteracion} ---")
            
            # Extraer almacén con menor distancia
            almacen_actual = avl.extraer_minimo()
            
            if almacen_actual is None or almacen_actual.distancia == float('inf'):
                print("  No hay más almacenes alcanzables")
                break
            
            print(f"  Procesando: {almacen_actual.id} "
                  f"(distancia actual: {almacen_actual.distancia})")
            
            # Marcar como visitado
            almacen_actual.visitado = True
            
            # Explorar rutas vecinas
            for vecino in almacen_actual.obtener_rutas():
                if not vecino.visitado:
                    distancia_ruta = almacen_actual.obtener_distancia_a(vecino)
                    nueva_distancia = almacen_actual.distancia + distancia_ruta
                    
                    print(f"    Vecino {vecino.id}: "
                          f"dist_actual={vecino.distancia}, "
                          f"nueva_dist={nueva_distancia}")
                    
                    # Si encontramos un camino más corto
                    if nueva_distancia < vecino.distancia:
                        print(f"      ¡Mejor camino encontrado! Actualizando...")
                        
                        # Eliminar del AVL con distancia antigua
                        clave_antigua = (vecino.distancia, vecino.id)
                        avl.eliminar(clave_antigua)
                        
                        # Actualizar distancia y predecesor
                        vecino.distancia = nueva_distancia
                        vecino.predecesor = almacen_actual
                        
                        # Reinsertar con nueva distancia
                        clave_nueva = (vecino.distancia, vecino.id)
                        avl.insertar(clave_nueva, vecino)
            
            print()
        
        # Paso 4: Construir resultados
        print("[Dijkstra] Construyendo resultados finales...")
        self._construir_resultados()
        
        return self.resultados
    
    def _construir_resultados(self):
        """Construye la tabla de resultados con distancias y caminos"""
        self.resultados = {}
        
        for id_almacen, almacen in self.grafo.nodos.items():
            camino = self._reconstruir_camino(almacen)
            
            self.resultados[id_almacen] = {
                'distancia': almacen.distancia,
                'camino': camino
            }
    
    def _reconstruir_camino(self, almacen_destino):
        """
        Reconstruye el camino desde el origen hasta el destino
        siguiendo los predecesores hacia atrás
        """
        if almacen_destino.distancia == float('inf'):
            return None  # No hay camino
        
        camino = []
        actual = almacen_destino
        
        while actual is not None:
            camino.insert(0, actual.id)  # Insertar al principio
            actual = actual.predecesor
        
        return camino
    
    def obtener_camino_a(self, destino_id):
        """Obtiene el resultado para un destino específico"""
        return self.resultados.get(destino_id, None)
    
    def mostrar_resultados(self):
        """Muestra todos los resultados de forma legible"""
        print("\n" + "="*70)
        print("RESULTADOS FINALES - CAMINOS MÁS CORTOS")
        print("="*70)
        print(f"{'Destino':<10} {'Distancia (km)':<15} {'Camino'}")
        print("-"*70)
        
        for id_almacen in sorted(self.resultados.keys()):
            resultado = self.resultados[id_almacen]
            distancia = resultado['distancia']
            camino = resultado['camino']
            
            if distancia == float('inf'):
                print(f"{id_almacen:<10} {'No alcanzable':<15} {'-'}")
            else:
                camino_str = " -> ".join(camino)
                print(f"{id_almacen:<10} {distancia:<15} {camino_str}")
        
        print("="*70 + "\n")


# ===================================================================================
# PASO 5: MAIN - RESOLVER EL PROBLEMA
# ===================================================================================

def main():
    """
    Función principal que resuelve el problema del enunciado
    """
    print("\n")
    print("#"*70)
    print("#  SOLUCIÓN DEL EJERCICIO: RED DE DISTRIBUCIÓN DE ALMACENES")
    print("#"*70)
    print()
    
    # =============== CREAR LA RED DE ALMACENES ===============
    print("PASO 1: Creando la red de almacenes...")
    print("-"*70)
    
    red = Grafo()
    
    # Agregar todas las rutas según el enunciado
    rutas = [
        ('A', 'B', 7),
        ('A', 'C', 9),
        ('A', 'F', 14),
        ('B', 'C', 10),
        ('B', 'D', 15),
        ('C', 'D', 11),
        ('C', 'F', 2),
        ('D', 'E', 6),
        ('E', 'F', 9)
    ]
    
    for origen, destino, distancia in rutas:
        red.agregar_ruta(origen, destino, distancia)
    
    # Mostrar la red completa
    print(red)
    
    # =============== EJECUTAR DIJKSTRA ===============
    print("\nPASO 2: Ejecutando algoritmo de Dijkstra...")
    print("-"*70)
    
    dijkstra = DijkstraConAVL(red)
    resultados = dijkstra.ejecutar('A')
    
    # =============== MOSTRAR RESULTADOS ===============
    print("\nPASO 3: Mostrando resultados...")
    print("-"*70)
    
    dijkstra.mostrar_resultados()
    
    # =============== CONSULTAS ESPECÍFICAS ===============
    print("\nCONSULTAS ESPECÍFICAS:")
    print("-"*70)
    
    destinos_interes = ['D', 'E', 'F']
    
    for destino in destinos_interes:
        info = dijkstra.obtener_camino_a(destino)
        if info:
            print(f"\nCamino más corto a almacén {destino}:")
            print(f"  Distancia total: {info['distancia']} km")
            print(f"  Ruta: {' -> '.join(info['camino'])}")
            
            # Calcular número de paradas
            num_paradas = len(info['camino']) - 1
            print(f"  Número de paradas intermedias: {num_paradas}")
    
    print("\n" + "="*70)
    print("EJERCICIO COMPLETADO")
    print("="*70 + "\n")


# ===================================================================================
# EJECUTAR
# ===================================================================================

if __name__ == "__main__":
    main()


# ===================================================================================
# NOTAS FINALES
# ===================================================================================
"""
PUNTOS CLAVE DE ESTA SOLUCIÓN:

1. ESTRUCTURA CLARA:
   - Nodos separados (AVL vs Grafo)
   - Cada clase con responsabilidad única
   - Métodos bien documentados

2. COMPLEJIDAD:
   - Dijkstra con AVL: O((V + E) log V)
   - Mejor que versión con lista: O(V²)
   - Cada operación AVL: O(log n)

3. BUENAS PRÁCTICAS POO:
   - Encapsulación (atributos privados con métodos)
   - Constructores __init__ completos
   - Métodos auxiliares privados (_prefijo)
   - __str__ para depuración

4. MANEJO DE CASOS ESPECIALES:
   - Nodos None en altura()
   - Distancia infinita para inalcanzables
   - Reinicialización antes de Dijkstra
   - Caminos con clave única (distancia, id)

5. DEBUG Y TRAZABILIDAD:
   - Prints informativos durante ejecución
   - Separación clara de pasos
   - Visualización de resultados

PARA EL EXAMEN:
- Memoriza la estructura de las clases
- Practica las rotaciones AVL a mano
- Entiende el flujo de Dijkstra
- Prueba con diferentes grafos
- Gestiona bien el tiempo (1 hora típico)

¡ÉXITO EN TU EXAMEN! 🚀
"""
