G = {"A", "B", "C", "D"}

from Graph import grafffo


def main():
    print("="*60)
    print("PRUEBA DE FUNCIONAMIENTO DE LA CLASE grafffo")
    print("="*60)
    
    # Crear un grafo
    print("\n>>> Creando un grafo vacío...")
    g = grafffo()
    
    # Agregar los nodos del conjunto G
    print("\n>>> Agregando nodos del conjunto G...")
    for nodo in G:
        g.agregar_nodo(nodo)
    
    # Intentar agregar un nodo duplicado
    print("\n>>> Intentando agregar un nodo duplicado...")
    g.agregar_nodo("A")
    
    # Agregar aristas
    print("\n>>> Agregando aristas...")
    g.agregar_arista("A", "B")
    g.agregar_arista("A", "C")
    g.agregar_arista("B", "D")
    g.agregar_arista("C", "D")
    g.agregar_arista("D", "A")
    
    # Intentar agregar arista con nodo inexistente
    print("\n>>> Intentando agregar arista con nodo inexistente...")
    g.agregar_arista("A", "E")
    g.agregar_arista("Z", "B")
    
    # Mostrar el grafo
    print("\n" + "="*60)
    print("GRAFO FINAL:")
    print("="*60)
    print(g)
    
    # Resumen del grafo
    print("\n" + "="*60)
    print("RESUMEN:")
    print("="*60)
    print(f"Nodos del conjunto G: {G}")
    print(f"Nodos en el grafo: {list(g.grafffo_dict.keys())}")
    print(f"Total de nodos: {len(g.grafffo_dict)}")
    print(f"Total de aristas: {sum(len(v) for v in g.grafffo_dict.values())}")
    
    # Mostrar conexiones
    print(f"\nConexiones:")
    for nodo, conexiones in g.grafffo_dict.items():
        if conexiones:
            print(f"  {nodo} → {conexiones}")
        else:
            print(f"  {nodo} → (sin conexiones)")


if __name__ == "__main__":
    main()
