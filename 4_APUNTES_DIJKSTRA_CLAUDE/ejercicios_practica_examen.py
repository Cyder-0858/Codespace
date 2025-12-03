"""
===================================================================================
EJERCICIOS DE PRÁCTICA Y CONSEJOS PARA EL EXAMEN
===================================================================================

IMPORTANTE: Este archivo contiene ejercicios para que practiques antes del examen
y consejos sobre qué esperar y cómo estructurar tus respuestas.
===================================================================================
"""


# ===================================================================================
# SECCIÓN 1: ESTRUCTURA GENERAL DE UN EJERCICIO TÍPICO DE EXAMEN
# ===================================================================================

"""
EJERCICIO TIPO: IMPLEMENTAR DIJKSTRA CON AVL

El ejercicio típicamente te pedirá:

1. DEFINIR LAS CLASES NECESARIAS:
   - class NodoArbol (o NodoAVL)
   - class NodoGrafo
   - class ArbolAVL (con todos sus métodos)
   - class Grafo
   - class Dijkstra (o el nombre que te den)

2. IMPLEMENTAR LOS MÉTODOS PRINCIPALES:
   - Constructor __init__ de cada clase
   - Métodos de inserción, eliminación, búsqueda
   - Rotaciones (simple derecha, simple izquierda)
   - Balanceo del AVL
   - Algoritmo de Dijkstra

3. INICIALIZAR Y EJECUTAR:
   - Crear instancias del grafo
   - Agregar nodos y aristas
   - Ejecutar Dijkstra desde un nodo origen
   - Mostrar resultados

ESTRUCTURA ESPERADA DE TU CÓDIGO:
"""

# Ejemplo de estructura básica esperada:

"""
# ============ PASO 1: DEFINIR NODOS ============
class NodoAVL:
    def __init__(self, clave, valor=None):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 0

class NodoGrafo:
    def __init__(self, identificador):
        self.id = identificador
        self.adyacentes = {}
        self.distancia = float('inf')
        self.predecesor = None
        self.visitado = False


# ============ PASO 2: ÁRBOL AVL ============
class ArbolAVL:
    def __init__(self):
        self.raiz = None
    
    def altura(self, nodo):
        # Tu código aquí
        pass
    
    def rotacion_derecha(self, nodo):
        # Tu código aquí
        pass
    
    def rotacion_izquierda(self, nodo):
        # Tu código aquí
        pass
    
    def balancear(self, nodo):
        # Tu código aquí
        pass
    
    def insertar(self, clave, valor=None):
        # Tu código aquí
        pass


# ============ PASO 3: GRAFO ============
class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, id):
        # Tu código aquí
        pass
    
    def agregar_arista(self, origen, destino, peso):
        # Tu código aquí
        pass


# ============ PASO 4: DIJKSTRA ============
class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def ejecutar(self, origen):
        # Tu código aquí
        pass


# ============ PASO 5: INICIALIZACIÓN Y EJECUCIÓN ============
# Crear grafo
g = Grafo()
g.agregar_arista('A', 'B', 4)
# ... más aristas

# Ejecutar Dijkstra
dijkstra = Dijkstra(g)
resultado = dijkstra.ejecutar('A')

# Mostrar resultados
# ...
"""


# ===================================================================================
# SECCIÓN 2: EJERCICIOS DE PRÁCTICA
# ===================================================================================

"""
========================
EJERCICIO 1: AVL BÁSICO
========================

Implementa un árbol AVL con las siguientes funcionalidades:

1. Clase NodoAVL con:
   - clave (int)
   - valor (cualquier tipo)
   - izquierdo, derecho (NodoAVL)
   - altura (int)

2. Clase ArbolAVL con:
   - insertar(clave, valor)
   - buscar(clave) -> NodoAVL
   - eliminar(clave)
   - inorden() -> lista
   - altura(nodo) -> int
   - factor_equilibrio(nodo) -> int
   - rotacion_derecha(nodo) -> NodoAVL
   - rotacion_izquierda(nodo) -> NodoAVL
   - balancear(nodo) -> NodoAVL

3. Prueba insertando: [50, 25, 75, 10, 30, 60, 80, 5]
4. Imprime recorrido inorden
5. Elimina 25 y vuelve a imprimir

PUNTOS CLAVE A RECORDAR:
- Después de insertar/eliminar SIEMPRE actualizar altura
- Después de actualizar altura SIEMPRE verificar balance
- Factor de equilibrio = altura(izq) - altura(der)
- Si |factor_equilibrio| > 1, hay que rotar

CASOS DE ROTACIÓN:
- balance > 1 y balance(hijo_izq) >= 0: Rotación derecha simple (LL)
- balance < -1 y balance(hijo_der) <= 0: Rotación izquierda simple (RR)
- balance > 1 y balance(hijo_izq) < 0: Rotación doble izq-der (LR)
- balance < -1 y balance(hijo_der) > 0: Rotación doble der-izq (RL)
"""


"""
=============================
EJERCICIO 2: GRAFO Y DIJKSTRA
=============================

Implementa un grafo dirigido y el algoritmo de Dijkstra:

1. Clase NodoGrafo con:
   - id (identificador único)
   - adyacentes (diccionario: {NodoGrafo: peso})
   - distancia (float, inicialmente inf)
   - predecesor (NodoGrafo, inicialmente None)
   - visitado (bool, inicialmente False)
   
   Métodos:
   - agregar_vecino(vecino, peso)
   - obtener_vecinos() -> lista
   - obtener_peso(vecino) -> float

2. Clase Grafo con:
   - nodos (diccionario: {id: NodoGrafo})
   
   Métodos:
   - agregar_nodo(id)
   - agregar_arista(origen, destino, peso)
   - obtener_nodo(id) -> NodoGrafo
   - reiniciar_nodos() (pone visitado=False, distancia=inf, predecesor=None)

3. Clase Dijkstra con:
   - grafo (Grafo)
   - caminos (diccionario con resultados)
   
   Métodos:
   - ejecutar(origen_id)
   - obtener_camino(destino_id)
   - imprimir_resultados()

4. Implementa Dijkstra usando UNA LISTA como cola de prioridad
   (versión simple sin heap ni AVL)

5. Prueba con este grafo:
   A -> B (4), A -> C (2)
   B -> C (1), B -> D (5)
   C -> D (8), C -> E (10)
   D -> E (2), D -> F (6)
   E -> F (3)
   
   Ejecuta desde 'A' y muestra todos los caminos más cortos.

PSEUDOCÓDIGO DE DIJKSTRA:
"""

def dijkstra_pseudocodigo(grafo, origen):
    """
    1. Inicializar:
       - distancia[origen] = 0
       - distancia[otros] = infinito
       - visitados = conjunto vacío
       - cola = todos los nodos
    
    2. Mientras cola no esté vacía:
       a) nodo_actual = nodo en cola con menor distancia
       b) marcar nodo_actual como visitado
       c) para cada vecino de nodo_actual:
          - si vecino no visitado:
            * nueva_dist = distancia[actual] + peso(actual, vecino)
            * si nueva_dist < distancia[vecino]:
              - distancia[vecino] = nueva_dist
              - predecesor[vecino] = nodo_actual
    
    3. Reconstruir caminos usando predecesores
    """
    pass


"""
=======================================
EJERCICIO 3: DIJKSTRA CON AVL COMPLETO
=======================================

Ahora combina ambos: implementa Dijkstra usando un AVL como cola de prioridad.

CONCEPTO CLAVE:
En lugar de usar una lista o heap para encontrar el nodo con menor distancia,
usamos un AVL donde:
- Clave = (distancia, id_nodo) 
- Valor = NodoGrafo

Ventaja del AVL:
- Inserción: O(log n)
- Extracción del mínimo: O(log n) (el nodo más a la izquierda)
- Disminuir prioridad: eliminar e insertar = 2 * O(log n)

PASOS:
1. Implementa todas las clases del Ejercicio 1 y 2
2. Modifica Dijkstra para usar AVL:
   
   class DijkstraConAVL:
       def __init__(self, grafo):
           self.grafo = grafo
           self.avl = ArbolAVL()
       
       def ejecutar(self, origen_id):
           # Inicializar distancias
           # Insertar todos los nodos en AVL con clave=(distancia, id)
           # Mientras AVL no vacío:
           #   - Extraer mínimo (más a la izquierda)
           #   - Procesar vecinos
           #   - Si distancia mejora:
           #     * Eliminar del AVL
           #     * Actualizar distancia
           #     * Reinsertar con nueva distancia

3. Prueba con el mismo grafo del Ejercicio 2
4. Compara resultados (deben ser idénticos)

TRUCO IMPORTANTE:
Para extraer el mínimo del AVL sin tener que implementar una función especial:
"""

def extraer_minimo_avl(avl):
    """Encuentra y elimina el nodo más a la izquierda"""
    if avl.arbol_vacio():
        return None
    
    # Ir hasta el nodo más a la izquierda
    nodo = avl.raiz
    while nodo.izquierdo is not None:
        nodo = nodo.izquierdo
    
    # Guardar valor
    valor = nodo.valor
    clave = nodo.clave
    
    # Eliminar del árbol
    avl.eliminar(clave)
    
    return valor


"""
=====================================
EJERCICIO 4: CASO EXAMEN COMPLETO
=====================================

ENUNCIADO SIMULADO:

"Se tiene un grafo dirigido que representa una red de ciudades conectadas
por carreteras con diferentes distancias. Implementa:

1. Una clase NodoAVL para crear un árbol AVL balanceado
2. Una clase ArbolAVL con todas las operaciones necesarias (insertar,
   eliminar, buscar, rotaciones, balanceo)
3. Una clase NodoGrafo para representar ciudades
4. Una clase Grafo para representar la red de carreteras
5. Una clase Dijkstra que use el AVL como estructura de datos auxiliar
   para encontrar los caminos más cortos desde una ciudad origen

El grafo debe permitir:
- Agregar ciudades (nodos)
- Agregar carreteras (aristas con peso = distancia)
- Ejecutar Dijkstra desde cualquier ciudad origen
- Mostrar el camino más corto hacia cualquier ciudad destino

Datos de prueba:
Ciudades: Madrid, Barcelona, Valencia, Sevilla, Bilbao

Carreteras (origen, destino, km):
Madrid -> Barcelona: 620
Madrid -> Valencia: 355
Madrid -> Sevilla: 530
Barcelona -> Valencia: 350
Barcelona -> Bilbao: 620
Valencia -> Sevilla: 650
Sevilla -> Valencia: 650
Bilbao -> Madrid: 395

Ejecutar Dijkstra desde Madrid y mostrar:
- Distancia mínima a cada ciudad
- Camino completo a cada ciudad"

TU TAREA:
Implementa TODO el código necesario siguiendo la estructura POO.
"""


# ===================================================================================
# SECCIÓN 3: CONSEJOS Y TIPS PARA EL EXAMEN
# ===================================================================================

"""
===============================
TIPS IMPORTANTES PARA EL EXAMEN
===============================

1. ESTRUCTURA DEL CÓDIGO:
   ✓ Define TODAS las clases primero
   ✓ Cada clase con su __init__ completo
   ✓ Usa nombres descriptivos (self.raiz, self.izquierdo, self.altura)
   ✓ Comenta casos especiales (rotación doble, nodo con dos hijos, etc.)

2. ORDEN DE IMPLEMENTACIÓN RECOMENDADO:
   a) NodoAVL y NodoGrafo (las estructuras básicas)
   b) Funciones auxiliares del AVL (altura, factor_equilibrio)
   c) Rotaciones del AVL (simple derecha, simple izquierda)
   d) Balanceo del AVL
   e) Insertar/buscar/eliminar del AVL
   f) Grafo (agregar_nodo, agregar_arista)
   g) Dijkstra (inicializar, bucle principal, reconstruir caminos)

3. ERRORES COMUNES A EVITAR:
   ✗ Olvidar actualizar altura después de rotar
   ✗ No manejar el caso de nodo None en altura()
   ✗ Confundir factor_equilibrio (debe ser altura_izq - altura_der)
   ✗ No verificar si un nodo existe antes de acceder a sus vecinos
   ✗ Olvidar inicializar distancia = infinito
   ✗ No reiniciar el grafo antes de ejecutar Dijkstra

4. CASOS ESPECIALES EN AVL:
   - Rotación LL: balance > 1 y hijo_izq tiene balance >= 0
   - Rotación RR: balance < -1 y hijo_der tiene balance <= 0  
   - Rotación LR: balance > 1 y hijo_izq tiene balance < 0
     (rotar hijo izq a la izquierda, luego nodo a la derecha)
   - Rotación RL: balance < -1 y hijo_der tiene balance > 0
     (rotar hijo der a la derecha, luego nodo a la izquierda)

5. CASOS ESPECIALES EN DIJKSTRA:
   - Nodo origen: distancia = 0
   - Nodos no alcanzables: distancia = infinito
   - Reconstruir camino: seguir predecesores desde destino hasta origen

6. GESTIÓN DEL TIEMPO:
   - Lee TODO el enunciado primero (5 min)
   - Planifica estructura de clases (5 min)
   - Implementa clase por clase (30-40 min)
   - Prueba con datos del enunciado (10 min)
   - Revisa y corrige errores (10 min)

7. SI TE ATASCAS:
   - Implementa la versión más simple primero
   - Deja comentarios: "# TODO: implementar rotación doble"
   - Sigue con otra parte y vuelve después
   - Asegúrate de que al menos compila sin errores

8. FORMATO DE SALIDA TÍPICO:
"""

# Ejemplo de cómo mostrar resultados:
def mostrar_resultados_ejemplo():
    print("="*50)
    print("CAMINOS MÁS CORTOS DESDE MADRID")
    print("="*50)
    print(f"{'Ciudad':<15} {'Distancia':>10} {'Camino'}")
    print("-"*50)
    print(f"{'Barcelona':<15} {620:>10} {'Madrid -> Barcelona'}")
    print(f"{'Valencia':<15} {355:>10} {'Madrid -> Valencia'}")
    # etc...


"""
===========================
CHECKLIST ANTES DE ENTREGAR
===========================

□ Todas las clases definidas con __init__
□ NodoAVL tiene: clave, valor, izquierdo, derecho, altura
□ NodoGrafo tiene: id, adyacentes, distancia, predecesor, visitado
□ ArbolAVL tiene: altura(), rotaciones, balancear(), insertar(), buscar()
□ Grafo tiene: agregar_nodo(), agregar_arista()
□ Dijkstra tiene: ejecutar(), reconstruir_caminos()
□ Se inicializa correctamente el grafo con los datos del enunciado
□ Se ejecuta Dijkstra desde el nodo origen especificado
□ Se muestran los resultados de forma clara
□ El código compila sin errores
□ NO se usan librerías externas (import math está OK para inf)
□ Todo está orientado a objetos (POO)

===========================
FRASES CLAVE PARA RECORDAR
===========================

"El AVL se balancea después de cada inserción y eliminación"
"Factor de equilibrio = altura(izquierda) - altura(derecha)"
"Si |factor_equilibrio| > 1, necesito rotar"
"Dijkstra siempre procesa el nodo con menor distancia"
"Los nodos visitados nunca se vuelven a procesar"
"La distancia al origen siempre es 0"
"Reconstruyo el camino siguiendo predecesores hacia atrás"
"""


# ===================================================================================
# SECCIÓN 4: PLANTILLA RÁPIDA PARA COPIAR EN EL EXAMEN
# ===================================================================================

"""
PLANTILLA BÁSICA (puedes copiar esta estructura y rellenar):
"""

# =============== NODOS ===============
class NodoAVL:
    def __init__(self, clave, valor=None):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 0

class NodoGrafo:
    def __init__(self, identificador):
        self.id = identificador
        self.adyacentes = {}
        self.distancia = float('inf')
        self.predecesor = None
        self.visitado = False
    
    def agregar_vecino(self, vecino, peso):
        self.adyacentes[vecino] = peso


# =============== AVL ===============
class ArbolAVL:
    def __init__(self):
        self.raiz = None
    
    def altura(self, nodo):
        return -1 if nodo is None else nodo.altura
    
    def actualizar_altura(self, nodo):
        if nodo:
            nodo.altura = 1 + max(self.altura(nodo.izquierdo), 
                                   self.altura(nodo.derecho))
    
    def factor_equilibrio(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)
    
    def rotacion_derecha(self, z):
        y = z.izquierdo
        T3 = y.derecho
        y.derecho = z
        z.izquierdo = T3
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        return y
    
    def rotacion_izquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo
        y.izquierdo = z
        z.derecho = T2
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        return y
    
    def balancear(self, nodo):
        if nodo is None:
            return nodo
        
        self.actualizar_altura(nodo)
        balance = self.factor_equilibrio(nodo)
        
        # LL
        if balance > 1 and self.factor_equilibrio(nodo.izquierdo) >= 0:
            return self.rotacion_derecha(nodo)
        
        # RR
        if balance < -1 and self.factor_equilibrio(nodo.derecho) <= 0:
            return self.rotacion_izquierda(nodo)
        
        # LR
        if balance > 1 and self.factor_equilibrio(nodo.izquierdo) < 0:
            nodo.izquierdo = self.rotacion_izquierda(nodo.izquierdo)
            return self.rotacion_derecha(nodo)
        
        # RL
        if balance < -1 and self.factor_equilibrio(nodo.derecho) > 0:
            nodo.derecho = self.rotacion_derecha(nodo.derecho)
            return self.rotacion_izquierda(nodo)
        
        return nodo
    
    def insertar(self, clave, valor=None):
        self.raiz = self._insertar_rec(self.raiz, clave, valor)
    
    def _insertar_rec(self, nodo, clave, valor):
        if nodo is None:
            return NodoAVL(clave, valor)
        
        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_rec(nodo.derecho, clave, valor)
        else:
            nodo.valor = valor
            return nodo
        
        return self.balancear(nodo)
    
    def arbol_vacio(self):
        return self.raiz is None


# =============== GRAFO ===============
class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, id):
        if id not in self.nodos:
            self.nodos[id] = NodoGrafo(id)
    
    def agregar_arista(self, origen, destino, peso):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        self.nodos[origen].agregar_vecino(self.nodos[destino], peso)
    
    def reiniciar(self):
        for nodo in self.nodos.values():
            nodo.visitado = False
            nodo.distancia = float('inf')
            nodo.predecesor = None


# =============== DIJKSTRA ===============
class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
        self.caminos = {}
    
    def ejecutar(self, origen_id):
        self.grafo.reiniciar()
        origen = self.grafo.nodos[origen_id]
        origen.distancia = 0
        
        no_visitados = list(self.grafo.nodos.values())
        
        while no_visitados:
            # Encontrar nodo con menor distancia
            nodo_actual = min(no_visitados, key=lambda n: n.distancia)
            
            if nodo_actual.distancia == float('inf'):
                break
            
            nodo_actual.visitado = True
            no_visitados.remove(nodo_actual)
            
            # Procesar vecinos
            for vecino, peso in nodo_actual.adyacentes.items():
                if not vecino.visitado:
                    nueva_dist = nodo_actual.distancia + peso
                    if nueva_dist < vecino.distancia:
                        vecino.distancia = nueva_dist
                        vecino.predecesor = nodo_actual
        
        self._construir_caminos()
    
    def _construir_caminos(self):
        for id_nodo, nodo in self.grafo.nodos.items():
            camino = []
            actual = nodo
            while actual:
                camino.insert(0, actual.id)
                actual = actual.predecesor
            
            self.caminos[id_nodo] = {
                'distancia': nodo.distancia,
                'camino': camino if nodo.distancia != float('inf') else None
            }
    
    def mostrar_resultados(self):
        print("\nRESULTADOS DIJKSTRA:")
        print("-" * 50)
        for nodo_id in sorted(self.caminos.keys()):
            info = self.caminos[nodo_id]
            if info['distancia'] == float('inf'):
                print(f"{nodo_id}: No alcanzable")
            else:
                camino = " -> ".join(info['camino'])
                print(f"{nodo_id}: {info['distancia']} | {camino}")


# =============== MAIN ===============
if __name__ == "__main__":
    # Crear grafo
    g = Grafo()
    
    # Agregar aristas (MODIFICA CON DATOS DEL ENUNCIADO)
    g.agregar_arista('A', 'B', 4)
    g.agregar_arista('A', 'C', 2)
    # ... más aristas
    
    # Ejecutar Dijkstra
    dijkstra = Dijkstra(g)
    dijkstra.ejecutar('A')  # Cambia 'A' por el origen del enunciado
    dijkstra.mostrar_resultados()


"""
¡MUCHA SUERTE EN EL EXAMEN!

Recuerda:
- Lee bien el enunciado
- Planifica antes de escribir
- POO puro, sin librerías
- Prueba tu código
- Gestiona bien el tiempo

¡Tú puedes! 💪
"""
