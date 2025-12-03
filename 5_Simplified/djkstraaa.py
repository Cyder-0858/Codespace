"""
Grafo Genérico con Árbol AVL
Implementación usando POO y TDA (Tipo de Dato Abstracto)
Sin librerías externas
"""


class NodoAVL:
    """Nodo del árbol AVL que representa un vértice del grafo"""
    
    def __init__(self, vertice):
        self.vertice = vertice
        self.altura = 1
        self.izquierdo = None
        self.derecho = None
        self.adyacentes = []  # Lista de vértices adyacentes


class ArbolAVL:
    """Árbol AVL para almacenar vértices del grafo de forma ordenada"""
    
    def __init__(self):
        self.raiz = None
    
    def obtener_altura(self, nodo):
        """Retorna la altura de un nodo"""
        if not nodo:
            return 0
        return nodo.altura
    
    def obtener_balance(self, nodo):
        """Calcula el factor de balance de un nodo"""
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho)
    
    def actualizar_altura(self, nodo):
        """Actualiza la altura de un nodo"""
        if nodo:
            nodo.altura = 1 + max(self.obtener_altura(nodo.izquierdo),
                                  self.obtener_altura(nodo.derecho))
    
    def rotar_derecha(self, z):
        """Rotación simple a la derecha"""
        y = z.izquierdo
        T3 = y.derecho
        
        y.derecho = z
        z.izquierdo = T3
        
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        
        return y
    
    def rotar_izquierda(self, z):
        """Rotación simple a la izquierda"""
        y = z.derecho
        T2 = y.izquierdo
        
        y.izquierdo = z
        z.derecho = T2
        
        self.actualizar_altura(z)
        self.actualizar_altura(y)
        
        return y
    
    def insertar(self, nodo, vertice):
        """Inserta un vértice en el árbol AVL"""
        # Inserción BST estándar
        if not nodo:
            return NodoAVL(vertice)
        
        if vertice < nodo.vertice:
            nodo.izquierdo = self.insertar(nodo.izquierdo, vertice)
        elif vertice > nodo.vertice:
            nodo.derecho = self.insertar(nodo.derecho, vertice)
        else:
            return nodo  # Vértice duplicado, no insertar
        
        # Actualizar altura
        self.actualizar_altura(nodo)
        
        # Obtener balance
        balance = self.obtener_balance(nodo)
        
        # Casos de desbalance
        # Caso Izquierda-Izquierda
        if balance > 1 and vertice < nodo.izquierdo.vertice:
            return self.rotar_derecha(nodo)
        
        # Caso Derecha-Derecha
        if balance < -1 and vertice > nodo.derecho.vertice:
            return self.rotar_izquierda(nodo)
        
        # Caso Izquierda-Derecha
        if balance > 1 and vertice > nodo.izquierdo.vertice:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)
        
        # Caso Derecha-Izquierda
        if balance < -1 and vertice < nodo.derecho.vertice:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)
        
        return nodo
    
    def buscar(self, nodo, vertice):
        """Busca un vértice en el árbol AVL"""
        if not nodo or nodo.vertice == vertice:
            return nodo
        
        if vertice < nodo.vertice:
            return self.buscar(nodo.izquierdo, vertice)
        return self.buscar(nodo.derecho, vertice)
    
    def obtener_minimo(self, nodo):
        """Obtiene el nodo con valor mínimo"""
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual
    
    def eliminar(self, nodo, vertice):
        """Elimina un vértice del árbol AVL"""
        if not nodo:
            return nodo
        
        # Búsqueda del nodo a eliminar
        if vertice < nodo.vertice:
            nodo.izquierdo = self.eliminar(nodo.izquierdo, vertice)
        elif vertice > nodo.vertice:
            nodo.derecho = self.eliminar(nodo.derecho, vertice)
        else:
            # Nodo encontrado
            if not nodo.izquierdo:
                return nodo.derecho
            elif not nodo.derecho:
                return nodo.izquierdo
            
            # Nodo con dos hijos
            temp = self.obtener_minimo(nodo.derecho)
            nodo.vertice = temp.vertice
            nodo.adyacentes = temp.adyacentes
            nodo.derecho = self.eliminar(nodo.derecho, temp.vertice)
        
        if not nodo:
            return nodo
        
        # Actualizar altura
        self.actualizar_altura(nodo)
        
        # Balancear
        balance = self.obtener_balance(nodo)
        
        # Casos de desbalance
        if balance > 1 and self.obtener_balance(nodo.izquierdo) >= 0:
            return self.rotar_derecha(nodo)
        
        if balance > 1 and self.obtener_balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)
        
        if balance < -1 and self.obtener_balance(nodo.derecho) <= 0:
            return self.rotar_izquierda(nodo)
        
        if balance < -1 and self.obtener_balance(nodo.derecho) > 0:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)
        
        return nodo
    
    def inorden(self, nodo, resultado):
        """Recorrido inorden del árbol"""
        if nodo:
            self.inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.vertice)
            self.inorden(nodo.derecho, resultado)


class Grafo:
    """Grafo genérico implementado con árbol AVL"""
    
    def __init__(self, dirigido=False):
        self.avl = ArbolAVL()
        self.dirigido = dirigido
        self.num_vertices = 0
        self.num_aristas = 0
    
    def agregar_vertice(self, vertice):
        """Agrega un vértice al grafo"""
        nodo_existente = self.avl.buscar(self.avl.raiz, vertice)
        if not nodo_existente:
            self.avl.raiz = self.avl.insertar(self.avl.raiz, vertice)
            self.num_vertices += 1
            return True
        return False
    
    def eliminar_vertice(self, vertice):
        """Elimina un vértice del grafo y todas sus aristas"""
        nodo = self.avl.buscar(self.avl.raiz, vertice)
        if not nodo:
            return False
        
        # Eliminar aristas que apuntan a este vértice
        self._eliminar_aristas_hacia_vertice(self.avl.raiz, vertice)
        
        # Contar aristas eliminadas
        self.num_aristas -= len(nodo.adyacentes)
        
        # Eliminar el vértice
        self.avl.raiz = self.avl.eliminar(self.avl.raiz, vertice)
        self.num_vertices -= 1
        return True
    
    def _eliminar_aristas_hacia_vertice(self, nodo, vertice_destino):
        """Método auxiliar para eliminar aristas que apuntan a un vértice"""
        if not nodo:
            return
        
        if vertice_destino in nodo.adyacentes:
            nodo.adyacentes.remove(vertice_destino)
            if not self.dirigido:
                self.num_aristas -= 1
        
        self._eliminar_aristas_hacia_vertice(nodo.izquierdo, vertice_destino)
        self._eliminar_aristas_hacia_vertice(nodo.derecho, vertice_destino)
    
    def agregar_arista(self, origen, destino):
        """Agrega una arista entre dos vértices"""
        nodo_origen = self.avl.buscar(self.avl.raiz, origen)
        nodo_destino = self.avl.buscar(self.avl.raiz, destino)
        
        if not nodo_origen or not nodo_destino:
            return False
        
        if destino not in nodo_origen.adyacentes:
            nodo_origen.adyacentes.append(destino)
            self.num_aristas += 1
            
            # Si el grafo no es dirigido, agregar arista inversa
            if not self.dirigido:
                if origen not in nodo_destino.adyacentes:
                    nodo_destino.adyacentes.append(origen)
            
            return True
        return False
    
    def eliminar_arista(self, origen, destino):
        """Elimina una arista entre dos vértices"""
        nodo_origen = self.avl.buscar(self.avl.raiz, origen)
        
        if not nodo_origen:
            return False
        
        if destino in nodo_origen.adyacentes:
            nodo_origen.adyacentes.remove(destino)
            self.num_aristas -= 1
            
            # Si el grafo no es dirigido, eliminar arista inversa
            if not self.dirigido:
                nodo_destino = self.avl.buscar(self.avl.raiz, destino)
                if nodo_destino and origen in nodo_destino.adyacentes:
                    nodo_destino.adyacentes.remove(origen)
            
            return True
        return False
    
    def existe_vertice(self, vertice):
        """Verifica si un vértice existe en el grafo"""
        return self.avl.buscar(self.avl.raiz, vertice) is not None
    
    def existe_arista(self, origen, destino):
        """Verifica si existe una arista entre dos vértices"""
        nodo = self.avl.buscar(self.avl.raiz, origen)
        if nodo:
            return destino in nodo.adyacentes
        return False
    
    def obtener_adyacentes(self, vertice):
        """Retorna la lista de vértices adyacentes a un vértice dado"""
        nodo = self.avl.buscar(self.avl.raiz, vertice)
        if nodo:
            return nodo.adyacentes.copy()
        return []
    
    def obtener_vertices(self):
        """Retorna todos los vértices del grafo en orden"""
        resultado = []
        self.avl.inorden(self.avl.raiz, resultado)
        return resultado
    
    def grado_vertice(self, vertice):
        """Retorna el grado de un vértice"""
        nodo = self.avl.buscar(self.avl.raiz, vertice)
        if nodo:
            return len(nodo.adyacentes)
        return 0
    
    def es_vacio(self):
        """Verifica si el grafo está vacío"""
        return self.num_vertices == 0
    
    def mostrar(self):
        """Muestra la representación del grafo"""
        vertices = self.obtener_vertices()
        print(f"\nGrafo {'Dirigido' if self.dirigido else 'No Dirigido'}")
        print(f"Vértices: {self.num_vertices}, Aristas: {self.num_aristas}")
        print("\nLista de adyacencia:")
        for vertice in vertices:
            adyacentes = self.obtener_adyacentes(vertice)
            print(f"{vertice} -> {adyacentes}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear grafo no dirigido
    print("=== GRAFO NO DIRIGIDO ===")
    g = Grafo(dirigido=False)
    
    # Agregar vértices
    vertices = [5, 3, 7, 2, 4, 6, 8]
    for v in vertices:
        g.agregar_vertice(v)
    
    # Agregar aristas
    aristas = [(5, 3), (5, 7), (3, 2), (3, 4), (7, 6), (7, 8)]
    for origen, destino in aristas:
        g.agregar_arista(origen, destino)
    
    g.mostrar()
    
    print(f"\n¿Existe vértice 5? {g.existe_vertice(5)}")
    print(f"¿Existe arista 5->3? {g.existe_arista(5, 3)}")
    print(f"Grado del vértice 5: {g.grado_vertice(5)}")
    
    # Crear grafo dirigido
    print("\n\n=== GRAFO DIRIGIDO ===")
    gd = Grafo(dirigido=True)
    
    vertices = ['A', 'B', 'C', 'D', 'E']
    for v in vertices:
        gd.agregar_vertice(v)
    
    aristas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    for origen, destino in aristas:
        gd.agregar_arista(origen, destino)
    
    gd.mostrar()
    
    print(f"\nAdyacentes de 'A': {gd.obtener_adyacentes('A')}")
    print(f"Adyacentes de 'D': {gd.obtener_adyacentes('D')}")