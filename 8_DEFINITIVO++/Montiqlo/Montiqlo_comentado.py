# ===========================================================
#                    TDA: NODO PRIORIDAD
# ===========================================================

class NodoPrioridad:
    """
    TDA auxiliar que representa un elemento en el montículo.
    
    ANALOGÍA: Piensa en una caja que contiene:
    - Una etiqueta de prioridad (número)
    - Un contenido (el dato real)
    
    En una sala de emergencias:
    - prioridad = gravedad del paciente (1-10)
    - dato = nombre del paciente
    """
    def __init__(self, prioridad, dato):
        """
        Constructor: crea un nodo con prioridad y dato.
        
        Parámetros:
        - prioridad: número que indica importancia (mayor = más urgente)
        - dato: el valor/información que queremos almacenar
        """
        self.prioridad = prioridad
        self.dato = dato

    def __repr__(self):
        """Representación en texto para facilitar debugging."""
        return f"Nodo(prioridad={self.prioridad}, dato={self.dato})"


# ===========================================================
#                    TDA: MONTÍCULO
# ===========================================================

class Monticulo:
    """
    TDA: Cola con prioridad implementada como montículo (Max-Heap).
    
    ¿QUÉ ES UN MONTÍCULO?
    Es un árbol binario que se almacena en un array/lista, donde:
    - El padre siempre tiene MAYOR prioridad que sus hijos (Max-Heap)
    - La raíz (posición 0) siempre tiene la MÁXIMA prioridad
    
    ESTRUCTURA EN ARRAY:
    Si tenemos el array: [9, 7, 5, 3, 2, 1]
    Representa este árbol:
    
              9
            /   \
           7     5
          / \   /
         3   2 1
    
    FÓRMULAS IMPORTANTES:
    Para un nodo en posición 'i':
    - Padre: (i - 1) // 2
    - Hijo izquierdo: 2 * i + 1
    - Hijo derecho: 2 * i + 2
    
    EJEMPLO VISUAL:
    Índices:  0   1   2   3   4   5
    Array:   [9,  7,  5,  3,  2,  1]
    
    Nodo 7 (índice 1):
    - Padre: (1-1)//2 = 0 → nodo 9
    - Hijo izq: 2*1+1 = 3 → nodo 3
    - Hijo der: 2*1+2 = 4 → nodo 2
    """
    
    def __init__(self):
        """
        Constructor: crea un montículo vacío usando una lista.
        
        DECISIÓN DE DISEÑO:
        Usamos una lista de Python (dinámica) en lugar de un array fijo.
        Ventaja: Crece automáticamente, no hay límite de capacidad.
        """
        self.heap = []  # Lista que almacena los NodoPrioridad

    # ===========================================================
    #           MÉTODOS AUXILIARES (HELPER METHODS)
    # ===========================================================

    def _indice_padre(self, indice):
        """
        Calcula el índice del padre de un nodo.
        
        FÓRMULA: (indice - 1) // 2
        
        EJEMPLO:
        - Nodo en posición 5 → padre en (5-1)//2 = 2
        - Nodo en posición 4 → padre en (4-1)//2 = 1
        - Nodo en posición 1 → padre en (1-1)//2 = 0 (la raíz)
        """
        return (indice - 1) // 2

    def _indice_hijo_izquierdo(self, indice):
        """
        Calcula el índice del hijo izquierdo de un nodo.
        
        FÓRMULA: 2 * indice + 1
        
        EJEMPLO:
        - Nodo en posición 0 → hijo izq en 2*0+1 = 1
        - Nodo en posición 1 → hijo izq en 2*1+1 = 3
        - Nodo en posición 2 → hijo izq en 2*2+1 = 5
        """
        return 2 * indice + 1

    def _indice_hijo_derecho(self, indice):
        """
        Calcula el índice del hijo derecho de un nodo.
        
        FÓRMULA: 2 * indice + 2
        
        EJEMPLO:
        - Nodo en posición 0 → hijo der en 2*0+2 = 2
        - Nodo en posición 1 → hijo der en 2*1+2 = 4
        - Nodo en posición 2 → hijo der en 2*2+2 = 6
        """
        return 2 * indice + 2

    def _tiene_padre(self, indice):
        """
        Verifica si un nodo tiene padre.
        
        LÓGICA: Solo la raíz (índice 0) no tiene padre.
        Todos los demás nodos tienen padre.
        """
        return indice > 0

    def _tiene_hijo_izquierdo(self, indice):
        """
        Verifica si un nodo tiene hijo izquierdo.
        
        LÓGICA: El hijo izquierdo existe si su índice está
        dentro del rango del heap.
        """
        return self._indice_hijo_izquierdo(indice) < len(self.heap)

    def _tiene_hijo_derecho(self, indice):
        """
        Verifica si un nodo tiene hijo derecho.
        
        LÓGICA: Similar al hijo izquierdo, verificamos que
        el índice calculado exista en el heap.
        """
        return self._indice_hijo_derecho(indice) < len(self.heap)

    def _intercambiar(self, indice1, indice2):
        """
        Intercambia dos elementos en el heap.
        
        TÉCNICA PYTHON: Usa asignación múltiple para intercambiar
        sin necesidad de variable temporal.
        
        EJEMPLO:
        heap = [5, 3, 8]
        _intercambiar(0, 2)
        heap = [8, 3, 5]  # 5 y 8 intercambiados
        """
        self.heap[indice1], self.heap[indice2] = \
            self.heap[indice2], self.heap[indice1]

    # ===========================================================
    #              OPERACIÓN: FLOTAR (SIFT UP)
    # ===========================================================

    def _flotar(self, indice):
        """
        OPERACIÓN FLOTAR: Mueve un elemento hacia ARRIBA en el heap
        mientras su prioridad sea MAYOR que la de su padre.
        
        ¿CUÁNDO SE USA?
        Después de AGREGAR un nuevo elemento al final del heap.
        
        ¿POR QUÉ SE LLAMA "FLOTAR"?
        Porque el elemento "sube" como una burbuja en agua,
        comparándose con su padre y intercambiándose si es mayor.
        
        ALGORITMO PASO A PASO:
        1. Empezar en el índice dado (normalmente el último elemento)
        2. MIENTRAS tenga padre:
           a. Calcular índice del padre
           b. SI mi prioridad > prioridad del padre:
              - Intercambiar conmigo y mi padre
              - Actualizar mi posición al índice del padre
           c. SI NO:
              - Ya estoy en la posición correcta, TERMINAR
        
        EJEMPLO VISUAL:
        
        Heap inicial:     [8, 6, 5, 3, 2]
                              8
                            /   \
                           6     5
                          / \
                         3   2
        
        Agregamos 10 al final:  [8, 6, 5, 3, 2, 10]
                              8
                            /   \
                           6     5
                          / \   /
                         3   2 10
        
        FLOTAR paso 1: 10 vs su padre 6
        - 10 > 6 → intercambiar
                              8
                            /   \
                          10     5
                          / \   /
                         3   2 6
        
        FLOTAR paso 2: 10 vs su nuevo padre 8
        - 10 > 8 → intercambiar
                             10
                            /   \
                           8     5
                          / \   /
                         3   2 6
        
        FLOTAR paso 3: 10 está en la raíz
        - No tiene padre → TERMINAR
        
        Resultado final:  [10, 8, 5, 3, 2, 6]
        """
        # Mientras el nodo tenga padre (no sea la raíz)
        while self._tiene_padre(indice):
            # Obtener el índice del padre
            indice_padre = self._indice_padre(indice)
            
            # Comparar prioridades: hijo vs padre
            if self.heap[indice].prioridad > self.heap[indice_padre].prioridad:
                # El hijo tiene MAYOR prioridad que el padre
                # → INTERCAMBIAR (el hijo "flota" hacia arriba)
                self._intercambiar(indice, indice_padre)
                
                # Actualizar la posición: ahora estoy donde estaba mi padre
                indice = indice_padre
            else:
                # Ya estoy en la posición correcta
                # (mi prioridad <= prioridad del padre)
                break

    # ===========================================================
    #             OPERACIÓN: HUNDIR (SIFT DOWN)
    # ===========================================================

    def _hundir(self, indice):
        """
        OPERACIÓN HUNDIR: Mueve un elemento hacia ABAJO en el heap
        mientras su prioridad sea MENOR que la de alguno de sus hijos.
        
        ¿CUÁNDO SE USA?
        Después de EXTRAER el elemento raíz (máxima prioridad).
        
        ¿POR QUÉ SE LLAMA "HUNDIR"?
        Porque el elemento "se hunde" como una piedra en agua,
        comparándose con sus hijos y intercambiándose con el mayor.
        
        ALGORITMO PASO A PASO:
        1. Empezar en el índice dado (normalmente la raíz = 0)
        2. MIENTRAS tenga al menos un hijo:
           a. Asumir que el hijo izquierdo es el mayor
           b. SI tiene hijo derecho Y su prioridad > hijo izquierdo:
              - Actualizar: el hijo derecho es el mayor
           c. SI el hijo mayor tiene prioridad > mi prioridad:
              - Intercambiar conmigo y el hijo mayor
              - Actualizar mi posición al índice del hijo
           d. SI NO:
              - Ya estoy en la posición correcta, TERMINAR
        
        REGLA IMPORTANTE:
        Siempre intercambiamos con el hijo de MAYOR prioridad,
        no con cualquier hijo. Esto mantiene la propiedad del heap.
        
        EJEMPLO VISUAL:
        
        Heap inicial:     [10, 8, 5, 3, 2, 6]
                             10
                            /   \
                           8     5
                          / \   /
                         3   2 6
        
        Extraemos 10 (raíz), movemos 6 a la raíz:
                              6
                            /   \
                           8     5
                          / \
                         3   2
        Array: [6, 8, 5, 3, 2]
        
        HUNDIR paso 1: 6 vs sus hijos (8 y 5)
        - Hijo mayor = 8
        - 6 < 8 → intercambiar con 8
                              8
                            /   \
                           6     5
                          / \
                         3   2
        
        HUNDIR paso 2: 6 vs sus hijos (3 y 2)
        - Hijo mayor = 3
        - 6 > 3 → NO intercambiar
        - TERMINAR (6 está en posición correcta)
        
        Resultado final:  [8, 6, 5, 3, 2]
                              8
                            /   \
                           6     5
                          / \
                         3   2
        """
        # Mientras el nodo tenga al menos un hijo izquierdo
        while self._tiene_hijo_izquierdo(indice):
            # Por defecto, asumimos que el hijo izquierdo es el mayor
            indice_hijo_mayor = self._indice_hijo_izquierdo(indice)
            
            # Verificar si existe hijo derecho
            if self._tiene_hijo_derecho(indice):
                indice_hijo_derecho = self._indice_hijo_derecho(indice)
                
                # Comparar: ¿el hijo derecho tiene mayor prioridad?
                if (self.heap[indice_hijo_derecho].prioridad > 
                    self.heap[indice_hijo_mayor].prioridad):
                    # Sí → actualizar cuál es el hijo mayor
                    indice_hijo_mayor = indice_hijo_derecho
            
            # Comparar el nodo actual con el hijo mayor
            if self.heap[indice].prioridad < self.heap[indice_hijo_mayor].prioridad:
                # El hijo tiene MAYOR prioridad que el padre
                # → INTERCAMBIAR (el padre "se hunde" hacia abajo)
                self._intercambiar(indice, indice_hijo_mayor)
                
                # Actualizar la posición: ahora estoy donde estaba mi hijo
                indice = indice_hijo_mayor
            else:
                # Ya estoy en la posición correcta
                # (mi prioridad >= prioridad de ambos hijos)
                break

    # ===========================================================
    #                  MÉTODO: AGREGAR
    # ===========================================================

    def agregar(self, dato, prioridad):
        """
        Agrega un nuevo elemento a la cola con prioridad.
        
        PROCESO COMPLETO:
        1. Crear un nuevo NodoPrioridad con el dato y prioridad
        2. Añadir el nodo al FINAL del heap (última posición)
        3. FLOTAR el nodo hasta que esté en su posición correcta
        
        ¿POR QUÉ AÑADIMOS AL FINAL?
        Para mantener la estructura de árbol binario completo.
        Un árbol binario completo se llena nivel por nivel,
        de izquierda a derecha.
        
        COMPLEJIDAD: O(log n)
        - Añadir al final: O(1)
        - Flotar: O(log n) en el peor caso (altura del árbol)
        
        EJEMPLO PASO A PASO:
        
        Heap inicial: [8, 6, 5, 3, 2]
                          8
                        /   \
                       6     5
                      / \
                     3   2
        
        agregar("Tarea A", 9):
        
        Paso 1: Añadir al final
        [8, 6, 5, 3, 2, 9]
                          8
                        /   \
                       6     5
                      / \   /
                     3   2 9
        
        Paso 2: Flotar 9
        - 9 > 5 (padre) → intercambiar
                          8
                        /   \
                       6     9
                      / \   /
                     3   2 5
        
        - 9 > 8 (nuevo padre) → intercambiar
                          9
                        /   \
                       6     8
                      / \   /
                     3   2 5
        
        Resultado: [9, 6, 8, 3, 2, 5]
        """
        # Crear el nodo con prioridad y dato
        nuevo_nodo = NodoPrioridad(prioridad, dato)
        
        # Añadir al final del heap
        self.heap.append(nuevo_nodo)
        
        # Flotar el nodo recién agregado hasta su posición correcta
        self._flotar(len(self.heap) - 1)

    # ===========================================================
    #                  MÉTODO: SIGUIENTE
    # ===========================================================

    def siguiente(self):
        """
        Extrae y retorna el elemento con MAYOR prioridad (la raíz).
        
        PROCESO COMPLETO:
        1. Verificar si el heap está vacío → retornar None
        2. Guardar el nodo raíz (tiene la máxima prioridad)
        3. Mover el ÚLTIMO elemento a la raíz
        4. Eliminar el último elemento del heap
        5. HUNDIR el nuevo elemento raíz hasta su posición correcta
        6. Retornar el dato del nodo original
        
        ¿POR QUÉ MOVEMOS EL ÚLTIMO A LA RAÍZ?
        - Mantiene la estructura de árbol binario completo
        - Solo necesitamos hundir UN elemento (más eficiente)
        - Alternativa sería reorganizar todo el árbol (muy lento)
        
        COMPLEJIDAD: O(log n)
        - Acceder a raíz: O(1)
        - Eliminar último: O(1)
        - Hundir: O(log n) en el peor caso
        
        EJEMPLO PASO A PASO:
        
        Heap inicial: [9, 6, 8, 3, 2, 5]
                          9
                        /   \
                       6     8
                      / \   /
                     3   2 5
        
        siguiente():
        
        Paso 1: Guardar raíz = 9
        
        Paso 2: Mover último (5) a la raíz
        [5, 6, 8, 3, 2]
                          5
                        /   \
                       6     8
                      / \
                     3   2
        
        Paso 3: Hundir 5
        - 5 vs hijos (6, 8) → hijo mayor = 8
        - 5 < 8 → intercambiar con 8
                          8
                        /   \
                       6     5
                      / \
                     3   2
        
        - 5 ya no tiene hijos → TERMINAR
        
        Resultado: [8, 6, 5, 3, 2]
        Retorno: 9 (dato del nodo extraído)
        """
        # Caso 1: Heap vacío
        if self.esta_vacio():
            return None
        
        # Paso 1: Guardar el nodo raíz (máxima prioridad)
        nodo_maximo = self.heap[0]
        
        # Paso 2: Obtener el último elemento y eliminarlo
        ultimo_nodo = self.heap.pop()
        
        # Paso 3: Si el heap no quedó vacío después de eliminar
        if not self.esta_vacio():
            # Mover el último elemento a la raíz
            self.heap[0] = ultimo_nodo
            
            # Hundir el nuevo elemento raíz
            self._hundir(0)
        
        # Paso 4: Retornar el dato del nodo máximo
        return nodo_maximo.dato

    # ===========================================================
    #                MÉTODOS AUXILIARES PÚBLICOS
    # ===========================================================

    def ver_maximo(self):
        """
        Retorna el elemento con mayor prioridad SIN extraerlo.
        
        ÚTIL PARA:
        - Ver cuál es el siguiente elemento sin eliminarlo
        - Verificar la prioridad antes de decidir si extraer
        
        DIFERENCIA CON siguiente():
        - ver_maximo(): Solo mira, no modifica el heap
        - siguiente(): Extrae y elimina el elemento
        """
        if self.esta_vacio():
            return None
        return self.heap[0].dato

    def ver_prioridad_maxima(self):
        """
        Retorna la prioridad del elemento máximo SIN extraerlo.
        """
        if self.esta_vacio():
            return None
        return self.heap[0].prioridad

    def esta_vacio(self):
        """
        Verifica si el heap está vacío.
        
        IMPLEMENTACIÓN: Simplemente verifica si la lista tiene elementos.
        len([]) = 0 → True (vacío)
        len([1, 2]) = 2 → False (no vacío)
        """
        return len(self.heap) == 0

    def tamanio(self):
        """
        Retorna el número de elementos en el heap.
        """
        return len(self.heap)

    def __repr__(self):
        """
        Representación en texto del heap para debugging.
        """
        return f"Monticulo(tamanio={len(self.heap)})"


# ===========================================================
#            EJEMPLO 1: USO BÁSICO DEL MONTÍCULO
# ===========================================================

def ejemplo_basico():
    """
    Ejemplo básico: Agregar y extraer elementos.
    """
    print("=" * 60)
    print("EJEMPLO 1: USO BÁSICO DEL MONTÍCULO")
    print("=" * 60)
    
    # Crear un montículo vacío
    cola = Monticulo()
    
    print("\n1. Agregando elementos:")
    print("-" * 40)
    
    # Agregar elementos con diferentes prioridades
    elementos = [
        ("Tarea A", 5),
        ("Tarea B", 2),
        ("Tarea C", 8),
        ("Tarea D", 1),
        ("Tarea E", 6)
    ]
    
    for dato, prioridad in elementos:
        cola.agregar(dato, prioridad)
        print(f"  Agregado: {dato} (prioridad {prioridad})")
        print(f"  Heap actual: {[n.prioridad for n in cola.heap]}")
    
    print(f"\n2. Tamaño del heap: {cola.tamanio()}")
    print(f"3. Elemento con mayor prioridad: {cola.ver_maximo()}")
    print(f"4. Prioridad máxima: {cola.ver_prioridad_maxima()}")
    
    print("\n5. Extrayendo elementos (de mayor a menor prioridad):")
    print("-" * 40)
    
    while not cola.esta_vacio():
        elemento = cola.siguiente()
        print(f"  Extraído: {elemento}")
        if not cola.esta_vacio():
            print(f"  Heap actual: {[n.prioridad for n in cola.heap]}")


# ===========================================================
#       EJEMPLO 2: SIMULACIÓN DE SALA DE EMERGENCIAS
# ===========================================================

def ejemplo_sala_emergencias():
    """
    Ejemplo práctico: Sala de emergencias de un hospital.
    Los pacientes se atienden según la gravedad (prioridad).
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 2: SALA DE EMERGENCIAS")
    print("=" * 60)
    
    emergencias = Monticulo()
    
    print("\nLlegada de pacientes:")
    print("-" * 40)
    
    pacientes = [
        ("Juan (dolor de cabeza)", 2),
        ("María (fractura grave)", 8),
        ("Pedro (resfriado)", 1),
        ("Ana (infarto)", 10),
        ("Luis (corte menor)", 3),
        ("Carmen (apendicitis)", 7)
    ]
    
    for paciente, gravedad in pacientes:
        emergencias.agregar(paciente, gravedad)
        print(f"  Llegó: {paciente} → Gravedad: {gravedad}/10")
    
    print(f"\nTotal de pacientes esperando: {emergencias.tamanio()}")
    print(f"Siguiente paciente: {emergencias.ver_maximo()} " +
          f"(gravedad: {emergencias.ver_prioridad_maxima()})")
    
    print("\nOrden de atención (por gravedad):")
    print("-" * 40)
    
    orden = 1
    while not emergencias.esta_vacio():
        paciente = emergencias.siguiente()
        print(f"  {orden}. {paciente}")
        orden += 1


# ===========================================================
#     EJEMPLO 3: VISUALIZACIÓN DE FLOTAR Y HUNDIR
# ===========================================================

def ejemplo_visualizacion():
    """
    Ejemplo que muestra paso a paso cómo funcionan flotar y hundir.
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 3: VISUALIZACIÓN DE FLOTAR Y HUNDIR")
    print("=" * 60)
    
    heap = Monticulo()
    
    print("\n--- DEMOSTRANDO FLOTAR ---")
    print("-" * 40)
    
    print("\nPaso 1: Heap vacío")
    print(f"  Array: []")
    
    print("\nPaso 2: Agregar 5")
    heap.agregar("A", 5)
    print(f"  Array: {[n.prioridad for n in heap.heap]}")
    print("  No necesita flotar (es la raíz)")
    
    print("\nPaso 3: Agregar 3")
    heap.agregar("B", 3)
    print(f"  Array: {[n.prioridad for n in heap.heap]}")
    print("  3 < 5 → No flota (hijo menor que padre)")
    
    print("\nPaso 4: Agregar 8")
    heap.agregar("C", 8)
    print(f"  Array antes de flotar: [5, 3, 8]")
    print("  8 > 5 (padre) → FLOTA")
    print(f"  Array después: {[n.prioridad for n in heap.heap]}")
    print("  Árbol:")
    print("      8")
    print("     / \\")
    print("    3   5")
    
    print("\nPaso 5: Agregar 10")
    heap.agregar("D", 10)
    print(f"  Array antes de flotar: [8, 10, 5, 3]")
    print("  10 > 8 (padre) → FLOTA")
    print(f"  Array después: {[n.prioridad for n in heap.heap]}")
    print("  Árbol:")
    print("      10")
    print("     /  \\")
    print("    8    5")
    print("   /")
    print("  3")
    
    print("\n--- DEMOSTRANDO HUNDIR ---")
    print("-" * 40)
    
    print("\nExtrayendo máximo (10):")
    heap.siguiente()
    print(f"  Array después de hundir: {[n.prioridad for n in heap.heap]}")
    print("  Proceso:")
    print("  1. Mover 3 a la raíz: [3, 8, 5]")
    print("  2. 3 < 8 (hijo mayor) → HUNDIR, intercambiar con 8")
    print("  3. Resultado: [8, 3, 5]")
    print("  Árbol:")
    print("      8")
    print("     / \\")
    print("    3   5")


# ===========================================================
#        EJEMPLO 4: COMPARACIÓN CON LISTA NO ORDENADA
# ===========================================================

def ejemplo_comparacion_eficiencia():
    """
    Compara la eficiencia del heap vs una lista simple.
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 4: ¿POR QUÉ USAR UN HEAP?")
    print("=" * 60)
    
    print("\nComparación de operaciones:")
    print("-" * 40)
    
    print("\nCON LISTA SIMPLE:")
    print("  Agregar elemento: O(1) - rápido")
    print("  Encontrar máximo: O(n) - LENTO (revisar toda la lista)")
    print("  Extraer máximo: O(n) - LENTO (encontrar y eliminar)")
    
    print("\nCON HEAP (MONTÍCULO):")
    print("  Agregar elemento: O(log n) - muy rápido")
    print("  Encontrar máximo: O(1) - INSTANTÁNEO (siempre en la raíz)")
    print("  Extraer máximo: O(log n) - muy rápido")
    
    print("\nEJEMPLO PRÁCTICO:")
    print("  Si tienes 1,000 elementos:")
    print("  - Lista: encontrar máximo requiere revisar 1,000 elementos")
    print("  - Heap: encontrar máximo requiere revisar 1 elemento")
    print("  - Heap: extraer máximo requiere ~10 operaciones (log₂ 1000)")


# ===========================================================
#           EJEMPLO 5: ALGORITMO DE DIJKSTRA
# ===========================================================

def ejemplo_dijkstra():
    """
    Ejemplo: Usar el heap como cola de prioridad en Dijkstra.
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 5: HEAP EN ALGORITMO DE DIJKSTRA")
    print("=" * 60)
    
    print("\nGrafo de ciudades:")
    print("-" * 40)
    print("  A --2-- B")
    print("  |       |")
    print("  4       3")
    print("  |       |")
    print("  C --1-- D")
    
    # Simulación simplificada de Dijkstra
    cola_prioridad = Monticulo()
    
    print("\nProceso de Dijkstra:")
    print("-" * 40)
    
    # Inicializar: distancia 0 a ciudad inicial A
    cola_prioridad.agregar("A", 0)
    print("1. Ciudad A con distancia 0 → cola: [(A, 0)]")
    
    # Explorar vecinos de A
    cola_prioridad.agregar("B", 2)  # A→B = 2
    cola_prioridad.agregar("C", 4)  # A→C = 4
    print("2. Explorar A → vecinos B(2) y C(4)")
    print(f"   Cola: {[(n.dato, n.prioridad) for n in cola_prioridad.heap]}")
    
    # Siguiente: B (menor distancia)
    ciudad = cola_prioridad.siguiente()
    print(f"3. Extraer {ciudad} (menor distancia)")
    
    # Explorar vecinos de B
    cola_prioridad.agregar("D", 5)  # A→B→D = 2+3 = 5
    print("4. Explorar B → vecino D(5)")
    print(f"   Cola: {[(n.dato, n.prioridad) for n in cola_prioridad.heap]}")
    
    print("\nVentaja del heap:")
    print("  ✓ Siempre extraemos la ciudad con menor distancia")
    print("  ✓ Operación en O(log n) en lugar de O(n)")


# ===========================================================
#                  EJEMPLO 6: SCHEDULER
# ===========================================================

def ejemplo_scheduler():
    """
    Ejemplo: Planificador de tareas (task scheduler).
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 6: PLANIFICADOR DE TAREAS")
    print("=" * 60)
    
    scheduler = Monticulo()
    
    print("\nTareas del sistema:")
    print("-" * 40)
    
    tareas = [
        ("Backup diario", 3),
        ("Actualizar antivirus", 8),
        ("Limpiar archivos temp", 1),
        ("Escanear sistema", 5),
        ("Actualizar SO", 9),
        ("Defragmentar disco", 2)
    ]
    
    for tarea, prioridad in tareas:
        scheduler.agregar(tarea, prioridad)
        print(f"  Añadida: {tarea} (prioridad {prioridad})")
    
    print(f"\nTareas en cola: {scheduler.tamanio()}")
    
    print("\nEjecutando tareas (por prioridad):")
    print("-" * 40)
    
    while not scheduler.esta_vacio():
        tarea = scheduler.siguiente()
        print(f"  ⚙️  Ejecutando: {tarea}")


# ===========================================================
#                  EJECUTAR TODOS LOS EJEMPLOS
# ===========================================================

if __name__ == "__main__":
    ejemplo_basico()
    ejemplo_sala_emergencias()
    ejemplo_visualizacion()
    ejemplo_comparacion_eficiencia()
    ejemplo_dijkstra()
    ejemplo_scheduler()
    
    print("\n" + "=" * 60)
    print("FIN DE LOS EJEMPLOS")
    print("=" * 60)
```

---

## **📚 Resumen de Conceptos Clave:**

### **1. ¿Qué es un Montículo?**
- Árbol binario almacenado en array
- Padre siempre mayor que hijos (Max-Heap)
- Raíz = elemento máximo

### **2. Fórmulas Esenciales:**
```
Padre de i:      (i - 1) // 2
Hijo izq de i:   2 * i + 1
Hijo der de i:   2 * i + 2