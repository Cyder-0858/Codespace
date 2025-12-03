"""
===================================================================================
CHEAT SHEET VISUAL - DIJKSTRA + AVL
===================================================================================

📋 RESUMEN RÁPIDO PARA EL EXAMEN
===================================================================================
"""


# ===================================================================================
# 1. ESTRUCTURA DE CLASES - PLANTILLA MÍNIMA
# ===================================================================================

ESTRUCTURA_MINIMA = """
┌─────────────────────────────────────────────────────────────┐
│                   ESTRUCTURA DE CLASES                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. NodoAVL                                                 │
│     ├── clave                                               │
│     ├── valor                                               │
│     ├── izquierdo                                           │
│     ├── derecho                                             │
│     └── altura                                              │
│                                                             │
│  2. NodoGrafo                                               │
│     ├── id                                                  │
│     ├── adyacentes (diccionario)                            │
│     ├── distancia                                           │
│     ├── predecesor                                          │
│     └── visitado                                            │
│                                                             │
│  3. ArbolAVL                                                │
│     ├── raiz                                                │
│     ├── altura(nodo)                                        │
│     ├── factor_equilibrio(nodo)                             │
│     ├── rotacion_derecha(nodo)                              │
│     ├── rotacion_izquierda(nodo)                            │
│     ├── balancear(nodo)                                     │
│     ├── insertar(clave, valor)                              │
│     └── eliminar(clave)                                     │
│                                                             │
│  4. Grafo                                                   │
│     ├── nodos (diccionario)                                 │
│     ├── agregar_nodo(id)                                    │
│     ├── agregar_arista(origen, destino, peso)               │
│     └── reiniciar_nodos()                                   │
│                                                             │
│  5. Dijkstra                                                │
│     ├── grafo                                               │
│     ├── ejecutar(origen)                                    │
│     └── reconstruir_caminos()                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
"""

print(ESTRUCTURA_MINIMA)


# ===================================================================================
# 2. CASOS DE ROTACIÓN AVL - DIAGRAMA VISUAL
# ===================================================================================

ROTACIONES_AVL = """
┌─────────────────────────────────────────────────────────────────────┐
│                    ROTACIONES AVL - 4 CASOS                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CASO 1: LL (Left-Left)                                             │
│  Condición: balance > 1 Y hijo_izq.balance >= 0                     │
│  Solución: Rotación simple DERECHA                                  │
│                                                                     │
│         z                        y                                  │
│        / \\                      / \\                                │
│       y   T4    -------->       x   z                               │
│      / \\                           / \\                             │
│     x   T3                        T3  T4                            │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CASO 2: RR (Right-Right)                                           │
│  Condición: balance < -1 Y hijo_der.balance <= 0                    │
│  Solución: Rotación simple IZQUIERDA                                │
│                                                                     │
│      z                             y                                │
│     / \\                           / \\                              │
│    T1  y       -------->          z   x                             │
│       / \\                        / \\                               │
│      T2  x                      T1  T2                              │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CASO 3: LR (Left-Right)                                            │
│  Condición: balance > 1 Y hijo_izq.balance < 0                      │
│  Solución: Rotación IZQ en hijo + Rotación DER en raíz              │
│                                                                     │
│       z              z                    x                         │
│      / \\            / \\                  / \\                       │
│     y   T4         x   T4               y   z                       │
│    / \\    --->    / \\       --->      / \\  / \\                    │
│   T1  x          y  T3               T1 T2 T3 T4                   │
│      / \\        / \\                                                │
│     T2 T3      T1 T2                                                │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CASO 4: RL (Right-Left)                                            │
│  Condición: balance < -1 Y hijo_der.balance > 0                     │
│  Solución: Rotación DER en hijo + Rotación IZQ en raíz              │
│                                                                     │
│     z                z                      x                       │
│    / \\              / \\                    / \\                     │
│   T1  y            T1  x                  z   y                     │
│      / \\    --->      / \\       --->    / \\ / \\                   │
│     x  T4            T2  y             T1 T2 T3 T4                 │
│    / \\                  / \\                                        │
│   T2 T3                T3 T4                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

💡 REGLA MNEMOTÉCNICA:
   - Si desbalance a la IZQUIERDA → rotar a la DERECHA
   - Si desbalance a la DERECHA → rotar a la IZQUIERDA
   - Si es "zigzag" (LR o RL) → necesitas DOS rotaciones
"""

print(ROTACIONES_AVL)


# ===================================================================================
# 3. ALGORITMO DE DIJKSTRA - FLUJO PASO A PASO
# ===================================================================================

FLUJO_DIJKSTRA = """
┌─────────────────────────────────────────────────────────────────────┐
│              ALGORITMO DE DIJKSTRA - PASO A PASO                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  INICIALIZACIÓN:                                                    │
│  ┌───────────────────────────────────────────────────────┐         │
│  │ 1. distancia[origen] = 0                              │         │
│  │ 2. distancia[todos los demás] = ∞                     │         │
│  │ 3. predecesor[todos] = None                           │         │
│  │ 4. visitado[todos] = False                            │         │
│  │ 5. Insertar todos en AVL (ordenados por distancia)    │         │
│  └───────────────────────────────────────────────────────┘         │
│                                                                     │
│  BUCLE PRINCIPAL:                                                   │
│  ┌───────────────────────────────────────────────────────┐         │
│  │ Mientras AVL no vacío:                                │         │
│  │                                                        │         │
│  │   PASO A: Extraer nodo con menor distancia            │         │
│  │   ├─> nodo_actual = extraer_minimo(AVL)               │         │
│  │   ├─> Si distancia == ∞: TERMINAR                     │         │
│  │   └─> marcar nodo_actual como VISITADO                │         │
│  │                                                        │         │
│  │   PASO B: Explorar vecinos                            │         │
│  │   ├─> Para cada vecino NO visitado:                   │         │
│  │   │                                                    │         │
│  │   │    PASO C: Calcular nueva distancia               │         │
│  │   │    ├─> nueva_dist = dist[actual] + peso_arista    │         │
│  │   │    │                                               │         │
│  │   │    PASO D: ¿Es mejor camino?                      │         │
│  │   │    └─> Si nueva_dist < dist[vecino]:              │         │
│  │   │        ├─> eliminar vecino del AVL                │         │
│  │   │        ├─> actualizar dist[vecino] = nueva_dist   │         │
│  │   │        ├─> actualizar predecesor[vecino] = actual │         │
│  │   │        └─> reinsertar vecino en AVL               │         │
│  │   │                                                    │         │
│  └───────────────────────────────────────────────────────┘         │
│                                                                     │
│  RECONSTRUCCIÓN DE CAMINOS:                                         │
│  ┌───────────────────────────────────────────────────────┐         │
│  │ Para cada nodo destino:                               │         │
│  │   camino = []                                          │         │
│  │   actual = destino                                     │         │
│  │   Mientras actual != None:                             │         │
│  │     camino.insertar_al_inicio(actual)                  │         │
│  │     actual = predecesor[actual]                        │         │
│  └───────────────────────────────────────────────────────┘         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

⏱️ COMPLEJIDAD:
   - Con AVL: O((V + E) log V)
   - Con lista: O(V²)
   - V = vértices, E = aristas

🔑 CLAVE: El AVL mantiene los nodos ordenados por distancia,
   permitiendo extraer el mínimo en O(log n) en lugar de O(n)
"""

print(FLUJO_DIJKSTRA)


# ===================================================================================
# 4. CÓDIGO MÍNIMO - COPIAR Y PEGAR
# ===================================================================================

CODIGO_MINIMO = '''
┌─────────────────────────────────────────────────────────────────────┐
│                  CÓDIGO MÍNIMO - TEMPLATE BASE                      │
└─────────────────────────────────────────────────────────────────────┘

# ===== PASO 1: NODOS =====
class NodoAVL:
    def __init__(self, clave, valor=None):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 0

class NodoGrafo:
    def __init__(self, id):
        self.id = id
        self.adyacentes = {}
        self.distancia = float('inf')
        self.predecesor = None
        self.visitado = False

# ===== PASO 2: AVL =====
class ArbolAVL:
    def __init__(self):
        self.raiz = None
    
    def altura(self, n):
        return -1 if n is None else n.altura
    
    def actualizar_altura(self, n):
        if n:
            n.altura = 1 + max(self.altura(n.izquierdo), self.altura(n.derecho))
    
    def factor_equilibrio(self, n):
        return 0 if n is None else self.altura(n.izquierdo) - self.altura(n.derecho)
    
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
    
    def balancear(self, n):
        if n is None: return n
        self.actualizar_altura(n)
        b = self.factor_equilibrio(n)
        
        # LL
        if b > 1 and self.factor_equilibrio(n.izquierdo) >= 0:
            return self.rotacion_derecha(n)
        # RR
        if b < -1 and self.factor_equilibrio(n.derecho) <= 0:
            return self.rotacion_izquierda(n)
        # LR
        if b > 1 and self.factor_equilibrio(n.izquierdo) < 0:
            n.izquierdo = self.rotacion_izquierda(n.izquierdo)
            return self.rotacion_derecha(n)
        # RL
        if b < -1 and self.factor_equilibrio(n.derecho) > 0:
            n.derecho = self.rotacion_derecha(n.derecho)
            return self.rotacion_izquierda(n)
        return n
    
    def insertar(self, clave, valor=None):
        self.raiz = self._ins(self.raiz, clave, valor)
    
    def _ins(self, n, k, v):
        if n is None: return NodoAVL(k, v)
        if k < n.clave: n.izquierdo = self._ins(n.izquierdo, k, v)
        elif k > n.clave: n.derecho = self._ins(n.derecho, k, v)
        else: n.valor = v; return n
        return self.balancear(n)
    
    def eliminar(self, clave):
        self.raiz = self._elim(self.raiz, clave)
    
    def _elim(self, n, k):
        if n is None: return None
        if k < n.clave: n.izquierdo = self._elim(n.izquierdo, k)
        elif k > n.clave: n.derecho = self._elim(n.derecho, k)
        else:
            if n.izquierdo is None: return n.derecho
            if n.derecho is None: return n.izquierdo
            s = self._min(n.derecho)
            n.clave, n.valor = s.clave, s.valor
            n.derecho = self._elim(n.derecho, s.clave)
        return self.balancear(n)
    
    def _min(self, n):
        while n.izquierdo: n = n.izquierdo
        return n
    
    def arbol_vacio(self):
        return self.raiz is None

# ===== PASO 3: GRAFO =====
class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, id):
        if id not in self.nodos:
            self.nodos[id] = NodoGrafo(id)
    
    def agregar_arista(self, o, d, p):
        self.agregar_nodo(o)
        self.agregar_nodo(d)
        self.nodos[o].adyacentes[self.nodos[d]] = p

# ===== PASO 4: DIJKSTRA =====
class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def ejecutar(self, origen):
        # Reiniciar
        for n in self.grafo.nodos.values():
            n.visitado = False
            n.distancia = float('inf')
            n.predecesor = None
        
        # Inicializar
        self.grafo.nodos[origen].distancia = 0
        avl = ArbolAVL()
        for n in self.grafo.nodos.values():
            avl.insertar((n.distancia, n.id), n)
        
        # Procesar
        while not avl.arbol_vacio():
            actual = self._extraer_min(avl)
            if actual.distancia == float('inf'): break
            actual.visitado = True
            
            for vecino, peso in actual.adyacentes.items():
                if not vecino.visitado:
                    nueva = actual.distancia + peso
                    if nueva < vecino.distancia:
                        avl.eliminar((vecino.distancia, vecino.id))
                        vecino.distancia = nueva
                        vecino.predecesor = actual
                        avl.insertar((vecino.distancia, vecino.id), vecino)
    
    def _extraer_min(self, avl):
        n = avl.raiz
        while n.izquierdo: n = n.izquierdo
        v = n.valor
        avl.eliminar(n.clave)
        return v

# ===== PASO 5: USAR =====
g = Grafo()
g.agregar_arista('A', 'B', 7)
# ... más aristas

d = Dijkstra(g)
d.ejecutar('A')
'''

print(CODIGO_MINIMO)


# ===================================================================================
# 5. ERRORES COMUNES Y CÓMO EVITARLOS
# ===================================================================================

ERRORES_COMUNES = """
┌─────────────────────────────────────────────────────────────────────┐
│                     ERRORES COMUNES ❌ → ✅                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. ALTURA                                                          │
│     ❌ return nodo.altura                                           │
│     ✅ return -1 if nodo is None else nodo.altura                   │
│                                                                     │
│  2. FACTOR DE EQUILIBRIO                                            │
│     ❌ return altura_der - altura_izq                               │
│     ✅ return altura_izq - altura_der                               │
│                                                                     │
│  3. ACTUALIZAR ALTURA                                               │
│     ❌ nodo.altura = max(izq.altura, der.altura)                    │
│     ✅ nodo.altura = 1 + max(altura(izq), altura(der))              │
│                                                                     │
│  4. OLVIDAR BALANCEAR                                               │
│     ❌ def insertar(): ... return nodo                              │
│     ✅ def insertar(): ... return self.balancear(nodo)              │
│                                                                     │
│  5. DISTANCIA INICIAL                                               │
│     ❌ self.distancia = 0                                           │
│     ✅ self.distancia = float('inf')  # Excepto origen = 0          │
│                                                                     │
│  6. NO REINICIAR GRAFO                                              │
│     ❌ dijkstra.ejecutar('A')  # segunda vez sin reiniciar          │
│     ✅ grafo.reiniciar(); dijkstra.ejecutar('A')                    │
│                                                                     │
│  7. CLAVE DEL AVL EN DIJKSTRA                                       │
│     ❌ avl.insertar(distancia, nodo)  # claves duplicadas!          │
│     ✅ avl.insertar((distancia, id), nodo)  # tupla única           │
│                                                                     │
│  8. RECONSTRUIR CAMINO                                              │
│     ❌ camino.append(actual)  # orden incorrecto                    │
│     ✅ camino.insert(0, actual)  # insertar al inicio               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
"""

print(ERRORES_COMUNES)


# ===================================================================================
# 6. CHECKLIST DE EXAMEN
# ===================================================================================

CHECKLIST = """
┌─────────────────────────────────────────────────────────────────────┐
│                      ✓ CHECKLIST FINAL                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ANTES DE EMPEZAR:                                                  │
│  □ Leer TODO el enunciado (5 min)                                   │
│  □ Identificar datos: nodos, aristas, origen                        │
│  □ Planificar estructura de clases                                  │
│                                                                     │
│  DURANTE LA IMPLEMENTACIÓN:                                         │
│  □ NodoAVL: clave, valor, izq, der, altura                          │
│  □ NodoGrafo: id, adyacentes, distancia, predecesor, visitado      │
│  □ ArbolAVL: altura(), factor_equilibrio()                          │
│  □ ArbolAVL: rotacion_derecha(), rotacion_izquierda()               │
│  □ ArbolAVL: balancear() con 4 casos                                │
│  □ ArbolAVL: insertar(), eliminar()                                 │
│  □ Grafo: agregar_nodo(), agregar_arista()                          │
│  □ Dijkstra: inicializar distancias                                 │
│  □ Dijkstra: bucle principal con AVL                                │
│  □ Dijkstra: actualizar distancias y predecesores                   │
│  □ Dijkstra: reconstruir caminos                                    │
│                                                                     │
│  INICIALIZACIÓN:                                                    │
│  □ Crear grafo: g = Grafo()                                         │
│  □ Agregar todas las aristas del enunciado                          │
│  □ Crear Dijkstra: d = Dijkstra(g)                                  │
│  □ Ejecutar: d.ejecutar(origen)                                     │
│  □ Mostrar resultados claramente                                    │
│                                                                     │
│  ANTES DE ENTREGAR:                                                 │
│  □ El código compila sin errores                                    │
│  □ No hay import (excepto math para inf, opcional)                  │
│  □ Todas las clases tienen __init__                                 │
│  □ Los resultados se muestran correctamente                         │
│  □ Revisé casos especiales (None, inf, etc.)                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
"""

print(CHECKLIST)


# ===================================================================================
# 7. REGLAS MNEMOTÉCNICAS
# ===================================================================================

MNEMONICAS = """
┌─────────────────────────────────────────────────────────────────────┐
│                  🧠 REGLAS MNEMOTÉCNICAS                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  PARA RECORDAR ROTACIONES AVL:                                      │
│  ┌───────────────────────────────────────────────────┐             │
│  │  "Si cae a la IZQUIERDA, gira a la DERECHA"       │             │
│  │  "Si cae a la DERECHA, gira a la IZQUIERDA"       │             │
│  │  "Si hace ZIGZAG, gira DOS VECES"                 │             │
│  └───────────────────────────────────────────────────┘             │
│                                                                     │
│  PARA RECORDAR FACTOR DE EQUILIBRIO:                                │
│  ┌───────────────────────────────────────────────────┐             │
│  │  FE = Izquierda - Derecha                          │             │
│  │  (piensa: "Left minus Right" = L - R)             │             │
│  │                                                    │             │
│  │  Si FE > 0: más pesado a la izquierda             │             │
│  │  Si FE < 0: más pesado a la derecha               │             │
│  │  Si |FE| > 1: DESBALANCEADO → rotar               │             │
│  └───────────────────────────────────────────────────┘             │
│                                                                     │
│  PARA RECORDAR DIJKSTRA:                                            │
│  ┌───────────────────────────────────────────────────┐             │
│  │  "SIEMPRE el más CERCANO primero"                 │             │
│  │  1. Saco el nodo con menor distancia              │             │
│  │  2. Miro sus vecinos                               │             │
│  │  3. Si encuentro camino más corto, actualizo      │             │
│  │  4. Los visitados NUNCA se vuelven a procesar     │             │
│  └───────────────────────────────────────────────────┘             │
│                                                                     │
│  PARA RECORDAR ALTURA:                                              │
│  ┌───────────────────────────────────────────────────┐             │
│  │  "Hoja tiene altura 0"                             │             │
│  │  "None tiene altura -1"                            │             │
│  │  "Padre = 1 + máximo de sus hijos"                │             │
│  └───────────────────────────────────────────────────┘             │
│                                                                     │
│  PARA RECORDAR CLAVE AVL EN DIJKSTRA:                               │
│  ┌───────────────────────────────────────────────────┐             │
│  │  "TUPLA para UNICIDAD"                             │             │
│  │  clave = (distancia, id)                           │             │
│  │  ├─> ordena por distancia primero                 │             │
│  │  └─> si empatan, ordena por id (desempate)        │             │
│  └───────────────────────────────────────────────────┘             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
"""

print(MNEMONICAS)


# ===================================================================================
# 8. COMPLEJIDADES - TABLA RESUMEN
# ===================================================================================

COMPLEJIDADES = """
┌─────────────────────────────────────────────────────────────────────┐
│              ⏱️  COMPLEJIDADES TEMPORALES                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ÁRBOL AVL:                                                         │
│  ┌────────────────────────────┬──────────────────┐                 │
│  │ Operación                  │ Complejidad      │                 │
│  ├────────────────────────────┼──────────────────┤                 │
│  │ Buscar                     │ O(log n)         │                 │
│  │ Insertar                   │ O(log n)         │                 │
│  │ Eliminar                   │ O(log n)         │                 │
│  │ Rotación simple            │ O(1)             │                 │
│  │ Rotación doble             │ O(1)             │                 │
│  │ Actualizar altura          │ O(1)             │                 │
│  │ Extraer mínimo             │ O(log n)         │                 │
│  └────────────────────────────┴──────────────────┘                 │
│                                                                     │
│  DIJKSTRA:                                                          │
│  ┌────────────────────────────┬──────────────────┐                 │
│  │ Versión                    │ Complejidad      │                 │
│  ├────────────────────────────┼──────────────────┤                 │
│  │ Con lista (naive)          │ O(V²)            │                 │
│  │ Con heap binario           │ O((V+E) log V)   │                 │
│  │ Con AVL                    │ O((V+E) log V)   │                 │
│  │ Con heap Fibonacci         │ O(E + V log V)   │                 │
│  └────────────────────────────┴──────────────────┘                 │
│                                                                     │
│  donde: V = vértices, E = aristas                                   │
│                                                                     │
│  ESPACIO:                                                           │
│  ┌────────────────────────────┬──────────────────┐                 │
│  │ Estructura                 │ Espacio          │                 │
│  ├────────────────────────────┼──────────────────┤                 │
│  │ AVL con n nodos            │ O(n)             │                 │
│  │ Grafo (lista adyacencia)   │ O(V + E)         │                 │
│  │ Dijkstra (estructuras)     │ O(V)             │                 │
│  └────────────────────────────┴──────────────────┘                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
"""

print(COMPLEJIDADES)


# ===================================================================================
# 9. TIPS FINALES
# ===================================================================================

TIPS_FINALES = """
┌─────────────────────────────────────────────────────────────────────┐
│                      💡 TIPS FINALES                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. GESTIÓN DEL TIEMPO (60 minutos típico):                         │
│     • 0-5 min: Leer enunciado completo                              │
│     • 5-10 min: Planificar estructura de clases                     │
│     • 10-40 min: Implementar (prioritario: AVL y Dijkstra)          │
│     • 40-50 min: Inicializar y probar con datos                     │
│     • 50-60 min: Revisar, corregir, comentar                        │
│                                                                     │
│  2. ORDEN DE IMPLEMENTACIÓN:                                        │
│     1º → Nodos (AVL y Grafo)                                        │
│     2º → Funciones auxiliares AVL (altura, FE)                      │
│     3º → Rotaciones AVL                                             │
│     4º → Balanceo AVL                                               │
│     5º → Insertar/eliminar AVL                                      │
│     6º → Grafo (agregar_nodo, agregar_arista)                       │
│     7º → Dijkstra (inicializar, bucle, reconstruir)                 │
│     8º → Main (crear grafo, ejecutar, mostrar)                      │
│                                                                     │
│  3. SI TE ATASCAS:                                                  │
│     • Deja comentarios: "# TODO: implementar esto"                  │
│     • Sigue con otra parte                                          │
│     • Asegúrate de que al menos compile                             │
│     • Implementa versión simple primero                             │
│                                                                     │
│  4. DEBUGGING RÁPIDO:                                               │
│     • Agrega prints temporales en puntos clave                      │
│     • Verifica que el grafo se crea bien                            │
│     • Imprime el AVL en cada paso de Dijkstra                       │
│     • Comprueba distancias después de cada iteración                │
│                                                                     │
│  5. PRESENTACIÓN:                                                   │
│     • Código limpio y bien indentado                                │
│     • Nombres descriptivos de variables                             │
│     • Comentarios en partes complejas                               │
│     • Resultado final claro y legible                               │
│                                                                     │
│  6. ANTES DE ENTREGAR:                                              │
│     ✓ Compila sin errores                                           │
│     ✓ No hay imports no permitidos                                  │
│     ✓ Todas las clases están completas                              │
│     ✓ Los resultados son correctos                                  │
│     ✓ El formato de salida es claro                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘


╔═════════════════════════════════════════════════════════════════════╗
║                                                                     ║
║              ¡MUCHA SUERTE EN TU EXAMEN! 🍀🎓                       ║
║                                                                     ║
║  Recuerda:                                                          ║
║  • Mantén la calma                                                  ║
║  • Lee bien el enunciado                                            ║
║  • Planifica antes de codificar                                     ║
║  • POO puro, sin librerías                                          ║
║  • Gestiona tu tiempo                                               ║
║  • ¡Tú puedes hacerlo! 💪                                           ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝
"""

print(TIPS_FINALES)
