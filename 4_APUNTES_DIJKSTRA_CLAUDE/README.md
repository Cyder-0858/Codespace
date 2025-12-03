# 📚 Material de Estudio - Examen Python POO + Dijkstra + AVL

## 🎯 Descripción

Material completo de preparación para examen de Python centrado en:
- **Programación Orientada a Objetos (POO)** pura
- **Tipos de Datos Abstractos (TDA)**
- **Algoritmo de Dijkstra** con optimización
- **Árboles AVL** auto-balanceados
- **Grafos** con lista de adyacencia

**🚫 RESTRICCIÓN IMPORTANTE:** Sin usar librerías externas (todo implementado desde cero)

---

## 📑 Contenido del Material

### 1️⃣ `guia_examen_dijkstra_avl.py` (29 KB)
**⭐ ARCHIVO PRINCIPAL - IMPLEMENTACIÓN COMPLETA**

Contiene:
- ✅ Clase `NodoArbolAVL` con todos sus atributos
- ✅ Clase `ArbolAVL` completa con:
  - Inserción, eliminación, búsqueda
  - Rotaciones simples (derecha e izquierda)
  - Balanceo automático (4 casos: LL, RR, LR, RL)
  - Cálculo de altura y factor de equilibrio
  - Recorridos: inorden, preorden, postorden
- ✅ Clase `NodoGrafo` para representar vértices
- ✅ Clase `Grafo` con lista de adyacencia
- ✅ Clase `ColaPrioridad` (heap mínimo)
- ✅ Clase `Dijkstra` estándar con heap
- ✅ Clase `DijkstraConAVL` (versión optimizada)
- ✅ Ejemplos funcionando y probados

**👉 Usa este archivo para estudiar las implementaciones completas**

---

### 2️⃣ `ejercicios_practica_examen.py` (20 KB)
**📝 EJERCICIOS Y PRÁCTICA**

Contiene:
- 📋 4 ejercicios progresivos:
  - Ejercicio 1: AVL básico
  - Ejercicio 2: Grafo y Dijkstra simple
  - Ejercicio 3: Dijkstra con AVL
  - Ejercicio 4: Caso completo tipo examen
- 💡 Tips y consejos para el examen
- ⚠️ Errores comunes a evitar
- ✓ Checklist antes de entregar
- 📦 Plantilla base lista para copiar

**👉 Usa este archivo para practicar antes del examen**

---

### 3️⃣ `ejercicio_resuelto_completo.py` (25 KB)
**✅ SOLUCIÓN PASO A PASO**

Contiene:
- 📖 Enunciado completo de ejemplo
- 🔍 Explicación detallada de cada paso
- 💻 Implementación completa comentada
- 🧪 Pruebas con datos reales
- 📊 Salida formateada y resultados
- 📝 Notas explicativas en cada sección

**Ejemplo resuelto:**
- Red de almacenes con 6 nodos
- 9 rutas con distancias
- Dijkstra desde almacén A
- Resultados verificados y correctos

**👉 Ejecuta este archivo para ver cómo funciona todo junto**

```bash
python3 ejercicio_resuelto_completo.py
```

---

### 4️⃣ `cheatsheet_visual.py` (43 KB)
**🎨 CHEAT SHEET VISUAL**

Contiene:
- 📐 Diagramas ASCII de rotaciones AVL
- 🔄 Flujo visual del algoritmo de Dijkstra
- 📋 Código mínimo listo para copiar
- 🧠 Reglas mnemotécnicas
- ⏱️ Tabla de complejidades
- ❌ Errores comunes con soluciones
- ✓ Checklist final

**👉 Imprime este archivo para tenerlo durante el estudio**

```bash
python3 cheatsheet_visual.py
```

---

## 🚀 Cómo Usar Este Material

### Fase 1: Entender (Día 1-2)
1. Lee `guia_examen_dijkstra_avl.py` línea por línea
2. Ejecuta los ejemplos para ver cómo funcionan
3. Estudia las rotaciones AVL con el cheatsheet visual
4. Entiende el flujo de Dijkstra

### Fase 2: Practicar (Día 3-4)
1. Intenta resolver los ejercicios de `ejercicios_practica_examen.py`
2. Compara con la solución en `ejercicio_resuelto_completo.py`
3. Reescribe las implementaciones sin mirar
4. Prueba con diferentes grafos

### Fase 3: Memorizar (Día 5)
1. Memoriza la estructura de clases con el cheatsheet
2. Practica las rotaciones AVL a mano
3. Repasa los casos de Dijkstra
4. Revisa el checklist final

### Fase 4: Simulacro (Día del examen)
1. Haz un simulacro cronometrado (60 min)
2. Usa solo el template base
3. No mires las soluciones
4. Practica la gestión del tiempo

---

## 🎯 Estructura Típica del Examen

```
┌──────────────────────────────────────────────────┐
│ EJERCICIO 1: Dijkstra con AVL (60 minutos)      │
├──────────────────────────────────────────────────┤
│                                                  │
│ 1. Definir clases (30 min):                     │
│    - NodoAVL                                     │
│    - NodoGrafo                                   │
│    - ArbolAVL (completo)                         │
│    - Grafo                                       │
│    - Dijkstra                                    │
│                                                  │
│ 2. Inicializar y ejecutar (20 min):             │
│    - Crear grafo con datos del enunciado        │
│    - Ejecutar Dijkstra desde origen              │
│    - Mostrar resultados                          │
│                                                  │
│ 3. Revisar y entregar (10 min):                 │
│    - Verificar que compile                       │
│    - Comprobar resultados                        │
│    - Agregar comentarios                         │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## ⚡ Quick Reference

### Clase NodoAVL
```python
class NodoAVL:
    def __init__(self, clave, valor=None):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 0
```

### Clase NodoGrafo
```python
class NodoGrafo:
    def __init__(self, id):
        self.id = id
        self.adyacentes = {}
        self.distancia = float('inf')
        self.predecesor = None
        self.visitado = False
```

### Factor de Equilibrio
```python
def factor_equilibrio(self, nodo):
    if nodo is None:
        return 0
    return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)
```

### Rotación Derecha
```python
def rotacion_derecha(self, z):
    y = z.izquierdo
    T3 = y.derecho
    y.derecho = z
    z.izquierdo = T3
    self.actualizar_altura(z)
    self.actualizar_altura(y)
    return y
```

### Dijkstra - Bucle Principal
```python
while not avl.arbol_vacio():
    nodo_actual = avl.extraer_minimo()
    if nodo_actual.distancia == float('inf'):
        break
    
    nodo_actual.visitado = True
    
    for vecino in nodo_actual.obtener_vecinos():
        if not vecino.visitado:
            nueva_dist = nodo_actual.distancia + peso_arista
            if nueva_dist < vecino.distancia:
                # Actualizar y reinsertar en AVL
                ...
```

---

## 📊 Complejidades

| Operación | AVL | Dijkstra (AVL) |
|-----------|-----|----------------|
| Insertar | O(log n) | - |
| Eliminar | O(log n) | - |
| Buscar | O(log n) | - |
| Algoritmo completo | - | O((V+E) log V) |

---

## ⚠️ Errores Comunes

### ❌ Error 1: Altura de None
```python
# MAL
return nodo.altura

# BIEN
return -1 if nodo is None else nodo.altura
```

### ❌ Error 2: Factor de Equilibrio
```python
# MAL
return altura_der - altura_izq

# BIEN
return altura_izq - altura_der
```

### ❌ Error 3: Olvidar Balancear
```python
# MAL
def insertar(self, nodo, clave):
    # ... inserción ...
    return nodo

# BIEN
def insertar(self, nodo, clave):
    # ... inserción ...
    return self.balancear(nodo)
```

---

## 📝 Checklist Pre-Examen

- [ ] Sé implementar las 4 rotaciones AVL
- [ ] Entiendo cuándo usar cada rotación
- [ ] Puedo calcular factor de equilibrio
- [ ] Conozco el flujo completo de Dijkstra
- [ ] Sé usar tuplas como claves en AVL
- [ ] Puedo reconstruir caminos con predecesores
- [ ] Manejo casos especiales (None, infinito)
- [ ] Tengo memorizada la estructura de clases

---

## 🎓 Conceptos Clave a Dominar

### AVL
- ✅ Auto-balanceo después de cada inserción/eliminación
- ✅ Factor de equilibrio: altura_izq - altura_der
- ✅ |FE| > 1 → necesita rotación
- ✅ 4 casos: LL, RR, LR, RL

### Dijkstra
- ✅ Procesa siempre el nodo con menor distancia
- ✅ Nodos visitados nunca se vuelven a procesar
- ✅ Distancia inicial: origen = 0, resto = ∞
- ✅ AVL mantiene nodos ordenados por distancia

### POO
- ✅ Todo debe estar en clases
- ✅ Cada clase con su `__init__`
- ✅ Métodos bien nombrados y comentados
- ✅ Sin librerías externas

---

## 💡 Consejos Finales

1. **Lee TODO el enunciado** antes de empezar a escribir
2. **Planifica 5 minutos** la estructura de clases
3. **Implementa en orden**: Nodos → AVL → Grafo → Dijkstra
4. **Prueba con los datos** del enunciado
5. **Gestiona tu tiempo**: 40 min código, 20 min pruebas
6. **Mantén la calma** si algo no funciona
7. **Escribe código limpio** con nombres descriptivos

---

## 🆘 Si Te Atascas

1. Deja comentarios: `# TODO: implementar rotación`
2. Sigue con otra parte y vuelve después
3. Asegúrate de que al menos compile
4. Implementa versión simple primero
5. No te rindas, cada punto cuenta

---

## 📞 Recursos Adicionales

- Apuntes del curso: `1_Orientado_a_objetos_POO_.docx`
- Apuntes de grafos: `Limpio_Arboles_y_grafos__1_.docx`

---

## ✅ Verificación Pre-Examen

Ejecuta cada archivo para verificar que funciona:

```bash
# Test 1: Implementaciones completas
python3 guia_examen_dijkstra_avl.py

# Test 2: Ejercicio resuelto
python3 ejercicio_resuelto_completo.py

# Test 3: Cheatsheet visual
python3 cheatsheet_visual.py
```

Si todos funcionan sin errores, ¡estás listo! 🎉

---

## 🏆 ¡Mucha Suerte!

Recuerda:
- Has estudiado bien
- Conoces el material
- Puedes hacerlo
- Mantén la calma
- Lee con atención
- Gestiona tu tiempo

**¡Tú puedes! 💪🚀**

---

## 📄 Licencia

Este material es para uso educativo personal.

---

**Última actualización:** Diciembre 2024
**Versión:** 1.0
