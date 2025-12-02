import random
from collections import defaultdict, deque

class Grafo:
    """Clase para representar un grafo dirigido."""
    def __init__(self):
        self.vertices = set()
        self.aristas = []  # Lista de tuplas (origen, destino, peso)
        self.adyacencia = defaultdict(list)  # {origen: [(destino, peso), ...]}

    def agregar_vertice(self, v):
        """Agrega un vértice al grafo."""
        self.vertices.add(v)

    def agregar_arista(self, origen, destino, peso):
        """Agrega una arista dirigida con peso."""
        self.aristas.append((origen, destino, peso))
        self.adyacencia[origen].append((destino, peso))
        # Asegurar que ambos vértices existen
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)

    def eliminar_vertice(self, v):
        """Elimina un vértice y todas sus aristas."""
        self.vertices.discard(v)
        self.aristas = [(o, d, p) for o, d, p in self.aristas if o != v and d != v]
        if v in self.adyacencia:
            del self.adyacencia[v]
        for lista in self.adyacencia.values():
            self.adyacencia[v] = [(d, p) for d, p in lista if d != v]

    def obtener_vertices_conectados(self):
        """Devuelve los vértices que tienen al menos una arista (entrada o salida)."""
        conectados = set()
        for o, d, p in self.aristas:
            conectados.add(o)
            conectados.add(d)
        return conectados

    def a_eliminar_desconectados(self):
        """Elimina vértices sin aristas entrantes ni salientes."""
        conectados = self.obtener_vertices_conectados()
        desconectados = self.vertices - conectados
        for v in desconectados:
            self.eliminar_vertice(v)
        return desconectados

    def b_nodo_mayor_aristas_salientes(self):
        """Devuelve los nodos con mayor cantidad de aristas salientes."""
        salidas = defaultdict(int)
        for o, d, p in self.aristas:
            salidas[o] += 1
        if not salidas:
            return []
        max_salidas = max(salidas.values())
        return [v for v, count in salidas.items() if count == max_salidas]

    def c_nodo_mayor_aristas_entrantes(self):
        """Devuelve los nodos con mayor cantidad de aristas entrantes."""
        entradas = defaultdict(int)
        for o, d, p in self.aristas:
            entradas[d] += 1
        if not entradas:
            return []
        max_entradas = max(entradas.values())
        return [v for v, count in entradas.items() if count == max_entradas]

    def d_vertices_sin_acceso(self):
        """Devuelve vértices desde los cuales no se puede acceder a otro vértice.
        (Nodos sin aristas salientes o cuyos destinos no permiten llegar a otros)"""
        sin_salida = set()
        for v in self.vertices:
            if v not in self.adyacencia or len(self.adyacencia[v]) == 0:
                sin_salida.add(v)
        return sin_salida

    def e_contar_vertices(self):
        """Devuelve la cantidad de vértices en el grafo."""
        return len(self.vertices)

    def f_vertices_con_ciclo_directo(self):
        """Devuelve vértices que tienen una arista a sí mismos."""
        con_ciclo = set()
        for o, d, p in self.aristas:
            if o == d:
                con_ciclo.add(o)
        return con_ciclo

    def g_arista_mas_larga(self):
        """Devuelve la(s) arista(s) con mayor peso."""
        if not self.aristas:
            return []
        max_peso = max(p for o, d, p in self.aristas)
        return [(o, d, p) for o, d, p in self.aristas if p == max_peso]

    def mostrar_grafo(self):
        """Imprime la información del grafo."""
        print(f"\nVértices: {sorted(self.vertices)}")
        print(f"Total de vértices: {len(self.vertices)}")
        print(f"Total de aristas: {len(self.aristas)}")
        print("\nAristas (origen -> destino : peso):")
        for o, d, p in sorted(self.aristas):
            print(f"  {o} -> {d} : {p}")

def crear_grafo_aleatorio():
    """Crea un grafo con 15 vértices y 30 aristas aleatorias."""
    g = Grafo()
    
    # 1. Generar 15 vértices aleatorios no repetidos (números del 1 al 100)
    vertices = random.sample(range(1, 101), 15)
    for v in vertices:
        g.agregar_vertice(v)
    
    # 2. Agregar 30 aristas no repetidas con pesos aleatorios
    aristas_generadas = set()
    intentos = 0
    while len(g.aristas) < 30 and intentos < 1000:
        origen = random.choice(vertices)
        destino = random.choice(vertices)
        arista = (origen, destino)
        
        if arista not in aristas_generadas:
            peso = random.randint(1, 100)
            g.agregar_arista(origen, destino, peso)
            aristas_generadas.add(arista)
        intentos += 1
    
    return g

def main():
    print("=" * 70)
    print("ANÁLISIS DE GRAFO DIRIGIDO ALEATORIO")
    print("=" * 70)
    
    # Crear grafo aleatorio
    g = crear_grafo_aleatorio()
    print("\n>>> GRAFO INICIAL:")
    g.mostrar_grafo()
    
    # a) Eliminar vértices desconectados
    print("\n" + "=" * 70)
    print("a) ELIMINAR VÉRTICES DESCONECTADOS")
    print("=" * 70)
    desconectados = g.a_eliminar_desconectados()
    print(f"Vértices eliminados: {sorted(desconectados) if desconectados else 'Ninguno'}")
    g.mostrar_grafo()
    
    # b) Nodo con mayor cantidad de aristas salientes
    print("\n" + "=" * 70)
    print("b) NODO CON MAYOR CANTIDAD DE ARISTAS SALIENTES")
    print("=" * 70)
    max_salientes = g.b_nodo_mayor_aristas_salientes()
    print(f"Nodo(s): {max_salientes}")
    for v in max_salientes:
        count = sum(1 for o, d, p in g.aristas if o == v)
        print(f"  Vértice {v}: {count} arista(s) saliente(s)")
    
    # c) Nodo con mayor cantidad de aristas entrantes
    print("\n" + "=" * 70)
    print("c) NODO CON MAYOR CANTIDAD DE ARISTAS ENTRANTES")
    print("=" * 70)
    max_entrantes = g.c_nodo_mayor_aristas_entrantes()
    print(f"Nodo(s): {max_entrantes}")
    for v in max_entrantes:
        count = sum(1 for o, d, p in g.aristas if d == v)
        print(f"  Vértice {v}: {count} arista(s) entrante(s)")
    
    # d) Vértices sin acceso a otro vértice
    print("\n" + "=" * 70)
    print("d) VÉRTICES SIN ACCESO A OTRO VÉRTICE (sin aristas salientes)")
    print("=" * 70)
    sin_acceso = g.d_vertices_sin_acceso()
    print(f"Vértices: {sorted(sin_acceso) if sin_acceso else 'Ninguno'}")
    
    # e) Contar vértices
    print("\n" + "=" * 70)
    print("e) CANTIDAD DE VÉRTICES EN EL GRAFO")
    print("=" * 70)
    print(f"Total de vértices: {g.e_contar_vertices()}")
    
    # f) Vértices con ciclo directo
    print("\n" + "=" * 70)
    print("f) VÉRTICES CON CICLO DIRECTO (arista a sí mismo)")
    print("=" * 70)
    con_ciclo = g.f_vertices_con_ciclo_directo()
    print(f"Vértices: {sorted(con_ciclo) if con_ciclo else 'Ninguno'}")
    
    # g) Arista más larga
    print("\n" + "=" * 70)
    print("g) ARISTA(S) MÁS LARGA(S)")
    print("=" * 70)
    aristas_max = g.g_arista_mas_larga()
    if aristas_max:
        peso_max = aristas_max[0][2]
        print(f"Peso máximo: {peso_max}")
        for o, d, p in aristas_max:
            print(f"  {o} -> {d} : {p}")
    else:
        print("No hay aristas")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()