"""
===================================================================================
TEST DE AUTOEVALUACIÓN - ¿ESTÁS LISTO PARA EL EXAMEN?
===================================================================================

Este test te ayudará a evaluar si dominas los conceptos clave.
Responde mentalmente o en papel, luego verifica las respuestas al final.
===================================================================================
"""


print("="*70)
print("🎯 TEST DE AUTOEVALUACIÓN - DIJKSTRA + AVL")
print("="*70)
print("\n⏱️  Tiempo estimado: 20 minutos")
print("📝 Responde sin mirar los apuntes\n")
print("="*70)


# ===================================================================================
# SECCIÓN 1: AVL - CONCEPTOS BÁSICOS (10 preguntas)
# ===================================================================================

print("\n📘 SECCIÓN 1: AVL - CONCEPTOS BÁSICOS")
print("-"*70)

preguntas_avl = """
1. ¿Qué atributos debe tener un NodoAVL?
   a) Solo clave e hijos
   b) Clave, valor, hijos izq/der, altura
   c) Clave, valor, hijos, padre
   d) Clave, valor, peso

2. ¿Cómo se calcula el factor de equilibrio?
   a) altura_derecha - altura_izquierda
   b) altura_izquierda - altura_derecha
   c) altura_izquierda + altura_derecha
   d) max(altura_izq, altura_der)

3. ¿Qué altura tiene un nodo hoja?
   a) -1
   b) 0
   c) 1
   d) None

4. ¿Qué altura tiene un nodo None?
   a) -1
   b) 0
   c) 1
   d) infinito

5. ¿Cuándo está desbalanceado un nodo?
   a) Cuando FE = 0
   b) Cuando FE = 1
   c) Cuando |FE| > 1
   d) Cuando FE < 0

6. Caso LL (Left-Left): ¿qué rotación se aplica?
   a) Simple izquierda
   b) Simple derecha
   c) Doble (izq + der)
   d) Doble (der + izq)

7. Caso RR (Right-Right): ¿qué rotación se aplica?
   a) Simple izquierda
   b) Simple derecha
   c) Doble (izq + der)
   d) Doble (der + izq)

8. Caso LR (Left-Right): ¿qué rotación se aplica?
   a) Simple izquierda
   b) Simple derecha
   c) Primero izq en hijo, luego der en raíz
   d) Primero der en hijo, luego izq en raíz

9. ¿Cuándo se actualiza la altura de un nodo?
   a) Solo al insertar
   b) Solo al eliminar
   c) Después de insertar, eliminar o rotar
   d) Nunca, se calcula al vuelo

10. ¿Qué complejidad tiene buscar en un AVL?
    a) O(1)
    b) O(log n)
    c) O(n)
    d) O(n log n)
"""

print(preguntas_avl)


# ===================================================================================
# SECCIÓN 2: GRAFOS (5 preguntas)
# ===================================================================================

print("\n📗 SECCIÓN 2: GRAFOS")
print("-"*70)

preguntas_grafo = """
11. ¿Qué atributos debe tener un NodoGrafo para Dijkstra?
    a) Solo id y adyacentes
    b) id, adyacentes, distancia
    c) id, adyacentes, distancia, predecesor, visitado
    d) id, peso, vecinos

12. ¿Cómo se representa un grafo con lista de adyacencia?
    a) Matriz de booleanos
    b) Diccionario {id_nodo: NodoGrafo}
    c) Lista de listas
    d) Árbol binario

13. ¿Qué estructura usa adyacentes en NodoGrafo?
    a) Lista de tuplas
    b) Diccionario {vecino: peso}
    c) Conjunto de nodos
    d) Lista simple

14. ¿Cuál es la distancia inicial de los nodos en Dijkstra?
    a) 0 para todos
    b) 1 para todos
    c) 0 para origen, ∞ para el resto
    d) ∞ para todos

15. ¿Qué indica el atributo 'predecesor' en un nodo?
    a) Su altura en el árbol
    b) El nodo anterior en el camino más corto
    c) El primer nodo visitado
    d) Su padre en el grafo
"""

print(preguntas_grafo)


# ===================================================================================
# SECCIÓN 3: DIJKSTRA (10 preguntas)
# ===================================================================================

print("\n📕 SECCIÓN 3: DIJKSTRA")
print("-"*70)

preguntas_dijkstra = """
16. ¿Qué hace Dijkstra?
    a) Ordena un grafo
    b) Encuentra el camino más corto desde un origen
    c) Balancea un árbol
    d) Busca un elemento en un grafo

17. ¿En qué orden procesa Dijkstra los nodos?
    a) Orden alfabético
    b) Orden de inserción
    c) Orden de menor a mayor distancia
    d) Orden aleatorio

18. ¿Por qué usamos AVL en Dijkstra?
    a) Para guardar el grafo
    b) Para extraer el nodo con menor distancia en O(log n)
    c) Para balancear el grafo
    d) Para calcular distancias

19. ¿Qué clave usamos para insertar en el AVL de Dijkstra?
    a) Solo el id del nodo
    b) Solo la distancia
    c) Tupla (distancia, id)
    d) Tupla (id, distancia)

20. ¿Por qué usar tupla (distancia, id) y no solo distancia?
    a) Para hacer el AVL más rápido
    b) Para mantener unicidad de claves
    c) Para calcular mejor las distancias
    d) No hay razón específica

21. ¿Qué hacemos cuando encontramos un camino más corto?
    a) Solo actualizar la distancia
    b) Eliminar del AVL, actualizar, reinsertar
    c) Crear un nuevo nodo
    d) Rotar el AVL

22. ¿Se puede volver a procesar un nodo visitado?
    a) Sí, siempre
    b) Sí, si encontramos camino más corto
    c) No, nunca
    d) Depende del grafo

23. ¿Cómo reconstruimos el camino más corto?
    a) Siguiendo los hijos del árbol
    b) Siguiendo los predecesores desde destino a origen
    c) Usando BFS
    d) Ordenando por distancia

24. ¿Qué complejidad tiene Dijkstra con AVL?
    a) O(V²)
    b) O(V log V)
    c) O((V + E) log V)
    d) O(E log E)

25. ¿Qué significa si distancia[nodo] = ∞ después de Dijkstra?
    a) Error en el algoritmo
    b) Nodo no alcanzable desde origen
    c) Distancia muy grande
    d) Nodo no existe
"""

print(preguntas_dijkstra)


# ===================================================================================
# SECCIÓN 4: CÓDIGO - IDENTIFICA EL ERROR (5 preguntas)
# ===================================================================================

print("\n📙 SECCIÓN 4: CÓDIGO - IDENTIFICA EL ERROR")
print("-"*70)

codigo_errores = """
26. ¿Qué está mal aquí?
    ```
    def altura(self, nodo):
        return nodo.altura
    ```
    a) Nada, está bien
    b) No maneja el caso nodo = None
    c) Debería ser nodo.altura + 1
    d) Falta el return

27. ¿Qué está mal aquí?
    ```
    def factor_equilibrio(self, nodo):
        return self.altura(nodo.derecho) - self.altura(nodo.izquierdo)
    ```
    a) Nada, está bien
    b) El orden está invertido (debe ser izq - der)
    c) No maneja None
    d) Falta multiplicar por 2

28. ¿Qué está mal aquí?
    ```
    def insertar(self, nodo, clave):
        # ... código de inserción ...
        return nodo
    ```
    a) Nada, está bien
    b) Falta return self.balancear(nodo)
    c) Falta actualizar altura
    d) b y c son correctas

29. ¿Qué está mal aquí?
    ```
    def __init__(self):
        self.distancia = 0
        self.predecesor = None
        self.visitado = False
    ```
    a) Nada, está bien
    b) distancia debería ser float('inf')
    c) Falta el atributo id
    d) b y c son correctas

30. ¿Qué está mal aquí?
    ```
    # En Dijkstra
    avl.insertar(nodo.distancia, nodo)
    ```
    a) Nada, está bien
    b) Debería ser insertar(nodo, distancia)
    c) Debería ser insertar((distancia, id), nodo)
    d) Falta el valor
"""

print(codigo_errores)


# ===================================================================================
# RESPUESTAS
# ===================================================================================

print("\n" + "="*70)
print("📋 RESPUESTAS CORRECTAS")
print("="*70)

respuestas = """
SECCIÓN 1: AVL
1. b - Clave, valor, hijos izq/der, altura
2. b - altura_izquierda - altura_derecha
3. b - 0
4. a - -1
5. c - Cuando |FE| > 1
6. b - Simple derecha
7. a - Simple izquierda
8. c - Primero izq en hijo, luego der en raíz
9. c - Después de insertar, eliminar o rotar
10. b - O(log n)

SECCIÓN 2: GRAFOS
11. c - id, adyacentes, distancia, predecesor, visitado
12. b - Diccionario {id_nodo: NodoGrafo}
13. b - Diccionario {vecino: peso}
14. c - 0 para origen, ∞ para el resto
15. b - El nodo anterior en el camino más corto

SECCIÓN 3: DIJKSTRA
16. b - Encuentra el camino más corto desde un origen
17. c - Orden de menor a mayor distancia
18. b - Para extraer el nodo con menor distancia en O(log n)
19. c - Tupla (distancia, id)
20. b - Para mantener unicidad de claves
21. b - Eliminar del AVL, actualizar, reinsertar
22. c - No, nunca
23. b - Siguiendo los predecesores desde destino a origen
24. c - O((V + E) log V)
25. b - Nodo no alcanzable desde origen

SECCIÓN 4: CÓDIGO
26. b - No maneja el caso nodo = None
27. b - El orden está invertido (debe ser izq - der)
28. d - b y c son correctas (falta balancear)
29. d - b y c son correctas
30. c - Debería ser insertar((distancia, id), nodo)
"""

print(respuestas)


# ===================================================================================
# EVALUACIÓN
# ===================================================================================

print("\n" + "="*70)
print("📊 ESCALA DE EVALUACIÓN")
print("="*70)

evaluacion = """
Cuenta tus respuestas correctas:

🏆 27-30 correctas: ¡EXCELENTE! Estás más que listo
✅ 23-26 correctas: MUY BIEN - Repasa los fallos
⚠️  18-22 correctas: BIEN - Necesitas repasar algunos conceptos
⚡ 15-17 correctas: REGULAR - Estudia más los temas débiles
❌ Menos de 15: INSUFICIENTE - Repasa todo el material


RECOMENDACIONES SEGÚN TU RESULTADO:

🏆 27-30: 
   - Haz un simulacro completo cronometrado
   - Practica escribir código sin mirar apuntes
   - Repasa solo los casos especiales

✅ 23-26:
   - Repasa los temas que fallaste
   - Practica más ejercicios
   - Revisa el cheatsheet visual

⚠️  18-22:
   - Vuelve a leer la guía completa
   - Practica implementar AVL y Dijkstra desde cero
   - Resuelve el ejercicio completo sin ayuda

⚡ 15-17:
   - Dedica 1-2 días más de estudio
   - Lee línea por línea el código de ejemplo
   - Haz los 4 ejercicios de práctica

❌ Menos de 15:
   - Estudia los apuntes del curso primero
   - Entiende bien POO antes de continuar
   - Practica estructuras más simples (listas, pilas)
   - Dedica al menos 3 días más al material


PRÓXIMOS PASOS:
1. Anota tu puntuación: ___ / 30
2. Identifica tus puntos débiles
3. Repasa esos temas específicos
4. Vuelve a hacer el test en 24 horas
5. Objetivo: 27+ correctas antes del examen
"""

print(evaluacion)


print("\n" + "="*70)
print("💪 ¡SIGUE PRACTICANDO!")
print("="*70)
print("\nEl éxito está en la práctica constante.")
print("Cada error es una oportunidad de aprender.")
print("\n¡Tú puedes aprobar este examen! 🚀\n")
