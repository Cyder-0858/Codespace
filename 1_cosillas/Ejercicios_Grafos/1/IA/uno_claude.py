import random
from collections import defaultdict, deque

class GrafoDirigido:
    def __init__(self):
        self.grafo = defaultdict(list)
        self.vertices = set()
    
    def agregar_arista(self, origen, destino, etiqueta):
        self.grafo[origen].append((destino, etiqueta))
        self.vertices.add(origen)
        self.vertices.add(destino)
    
    def eliminar_desconectados(self):
        """a. Eliminar vértices desconectados (sin aristas entrantes ni salientes)"""
        vertices_con_aristas = set()
        
        # Vértices con aristas salientes
        for v in self.grafo:
            vertices_con_aristas.add(v)
        
        # Vértices con aristas entrantes
        for v in self.grafo:
            for destino, _ in self.grafo[v]:
                vertices_con_aristas.add(destino)
        
        vertices_desconectados = self.vertices - vertices_con_aristas
        self.vertices -= vertices_desconectados
        
        print(f"a. Vértices desconectados eliminados: {sorted(vertices_desconectados)}")
        print(f"   Total de vértices restantes: {len(self.vertices)}")
        return vertices_desconectados
    
    def nodo_mayor_salida(self):
        """b. Determinar el nodo con mayor cantidad de aristas que salen de él"""
        max_salidas = 0
        nodos_max = []
        
        for v in self.vertices:
            num_salidas = len(self.grafo[v])
            if num_salidas > max_salidas:
                max_salidas = num_salidas
                nodos_max = [v]
            elif num_salidas == max_salidas and num_salidas > 0:
                nodos_max.append(v)
        
        print(f"b. Nodo(s) con mayor cantidad de aristas salientes: {nodos_max}")
        print(f"   Cantidad de aristas salientes: {max_salidas}")
        return nodos_max, max_salidas
    
    def nodo_mayor_entrada(self):
        """c. Determinar el nodo con mayor cantidad de aristas que llegan a él"""
        entrada_count = defaultdict(int)
        
        for v in self.grafo:
            for destino, _ in self.grafo[v]:
                entrada_count[destino] += 1
        
        max_entradas = max(entrada_count.values()) if entrada_count else 0
        nodos_max = [v for v, count in entrada_count.items() if count == max_entradas]
        
        print(f"c. Nodo(s) con mayor cantidad de aristas entrantes: {nodos_max}")
        print(f"   Cantidad de aristas entrantes: {max_entradas}")
        return nodos_max, max_entradas
    
    def vertices_inaccesibles(self):
        """d. Indicar los vértices desde los cuales no se puede acceder a otro vértice"""
        vertices_sin_salida = []
        for v in self.vertices:
            if len(self.grafo[v]) == 0:
                vertices_sin_salida.append(v)
        
        print(f"d. Vértices desde los cuales no se puede acceder a otro: {sorted(vertices_sin_salida)}")
        print(f"   Total: {len(vertices_sin_salida)}")
        return vertices_sin_salida
    
    def contar_vertices(self):
        """e. Contar cuántos vértices componen el grafo"""
        total = len(self.vertices)
        print(f"e. Total de vértices en el grafo: {total}")
        return total
    
    def encontrar_ciclos_directos(self):
        """f. Determinar cuántos vértices tienen un arista a sí mismo (ciclo directo)"""
        ciclos = []
        for v in self.grafo:
            for destino, _ in self.grafo[v]:
                if destino == v:
                    ciclos.append(v)
                    break
        
        print(f"f. Vértices con ciclo directo (arista a sí mismo): {sorted(ciclos)}")
        print(f"   Total: {len(ciclos)}")
        return ciclos
    
    def arista_mas_larga(self):
        """g. Determinar la arista más larga, indicando su origen, destino y valor"""
        max_valor = -1
        aristas_max = []
        
        for origen in self.grafo:
            for destino, etiqueta in self.grafo[origen]:
                if etiqueta > max_valor:
                    max_valor = etiqueta
                    aristas_max = [(origen, destino, etiqueta)]
                elif etiqueta == max_valor:
                    aristas_max.append((origen, destino, etiqueta))
        
        print(f"g. Arista(s) más larga(s):")
        for origen, destino, valor in aristas_max:
            print(f"   Origen: {origen}, Destino: {destino}, Valor: {valor}")
        
        return aristas_max
    
    def mostrar_grafo(self):
        print("\n--- Estructura del Grafo ---")
        for v in sorted(self.vertices):
            if self.grafo[v]:
                aristas_str = ", ".join([f"{dest}(etiq:{etiq})" for dest, etiq in self.grafo[v]])
                print(f"Vértice {v}: -> {aristas_str}")
            else:
                print(f"Vértice {v}: sin aristas salientes")


def generar_grafo_aleatorio():
    """Genera un grafo con 15 vértices y 30 aristas aleatorias"""
    grafo = GrafoDirigido()
    
    # Generar 15 vértices aleatorios únicos
    vertices = random.sample(range(1, 101), 15)
    
    # Agregar vértices al grafo
    for v in vertices:
        grafo.vertices.add(v)
    
    # Generar 30 aristas aleatorias con etiquetas aleatorias
    for _ in range(30):
        origen = random.choice(vertices)
        destino = random.choice(vertices)
        etiqueta = random.randint(1, 100)
        grafo.agregar_arista(origen, destino, etiqueta)
    
    return grafo


# Programa principal
if __name__ == "__main__":
    print("=" * 60)
    print("GUÍA DE EJERCICIOS PRÁCTICOS - GRAFOS DIRIGIDOS")
    print("=" * 60)
    
    # Generar grafo aleatorio
    grafo = generar_grafo_aleatorio()
    
    print("\nGrafo inicial generado con 15 vértices y 30 aristas aleatorias")
    grafo.mostrar_grafo()
    
    print("\n" + "=" * 60)
    print("RESOLUCIÓN DE ACTIVIDADES")
    print("=" * 60 + "\n")
    
    # a. Eliminar vértices desconectados
    grafo.eliminar_desconectados()
    print()
    
    # b. Nodo con mayor cantidad de aristas salientes
    grafo.nodo_mayor_salida()
    print()
    
    # c. Nodo con mayor cantidad de aristas entrantes
    grafo.nodo_mayor_entrada()
    print()
    
    # d. Vértices inaccesibles
    grafo.vertices_inaccesibles()
    print()
    
    # e. Contar vértices
    grafo.contar_vertices()
    print()
    
    # f. Ciclos directos
    grafo.encontrar_ciclos_directos()
    print()
    
    # g. Arista más larga
    grafo.arista_mas_larga()
    
    print("\n" + "=" * 60)
    print("ANÁLISIS COMPLETADO")
    print("=" * 60)