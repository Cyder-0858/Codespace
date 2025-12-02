class Arista:
    def __init__(self, destino, peso):
        # 'destino' será una referencia al OBJETO Vertice, no solo el dato
        self.destino = destino  
        self.peso = peso

class Vertice:
    def __init__(self, dato):
        self.dato = dato
        # Lista de adyacencia: guardará objetos de tipo Arista
        self.vecinos = []

    def agregar_vecino(self, vertice_destino, peso):
        # Creamos la arista y la guardamos en la lista de este vértice
        nueva_arista = Arista(vertice_destino, peso)
        self.vecinos.append(nueva_arista)

class Grafo:
     def __init__(self, dirigido=False):
        self.dirigido = dirigido
        # Diccionario para acceder rápido a los vértices: { dato: ObjetoVertice }
        self.vertices = {}

    def agregar_vertice(self, dato):
        if dato not in self.vertices:
            self.vertices[dato] = Vertice(dato)
            return True
        return False

    def agregar_arista(self, dato_origen, dato_destino, peso):
        # Verificamos que ambos existan en nuestro diccionario
        if dato_origen in self.vertices and dato_destino in self.vertices:
            
            # Recuperamos los OBJETOS Vertice
            nodo_origen = self.vertices[dato_origen]
            nodo_destino = self.vertices[dato_destino]

            # Creamos la conexión A -> B
            nodo_origen.agregar_vecino(nodo_destino, peso)

            # Si el grafo NO es dirigido (ida y vuelta), creamos B -> A
            if not self.dirigido:
                nodo_destino.agregar_vecino(nodo_origen, peso)
        else:
            print(f"Error: No se pueden unir '{dato_origen}' y '{dato_destino}'. Uno no existe.")

    def imprimir_grafo(self):
        print(f"--- Grafo {'Dirigido' if self.dirigido else 'No Dirigido'} ---")
        for key in self.vertices:
            nodo = self.vertices[key]
            # Construimos un string para mostrar los vecinos
            conexiones = ""
            for arista in nodo.vecinos:
                conexiones += f"({arista.destino.dato}, p:{arista.peso}) "
            
            if not conexiones:
                conexiones = "Sin conexiones"
                
            print(f"[{nodo.dato}] -> {conexiones}")
        print("--------------------------------------")


# ==========================================
#              PRUEBAS (MAIN)
# ==========================================

# No necesitamos "if __name__ ==..." ni librerías, el código se ejecuta directo.

# --- EJEMPLO 1: Grafo con Strings (Ciudades) ---
print("EJEMPLO 1: Rutas de Ciudades")
mi_grafo = Grafo(dirigido=False) # False = Caminos de ida y vuelta

mi_grafo.agregar_vertice("Madrid")
mi_grafo.agregar_vertice("Bogotá")
mi_grafo.agregar_vertice("Lima")
mi_grafo.agregar_vertice("Buenos Aires")

# Conectamos con pesos (ej. horas de vuelo)
mi_grafo.agregar_arista("Madrid", "Bogotá", 10)
mi_grafo.agregar_arista("Bogotá", "Lima", 3)
mi_grafo.agregar_arista("Lima", "Buenos Aires", 4)
mi_grafo.agregar_arista("Madrid", "Buenos Aires", 12)

mi_grafo.imprimir_grafo()
print("\n")

# --- EJEMPLO 2: Grafo con Enteros (Red de Tuberías) ---
# Aquí demostramos que es GENÉRICO: Usamos 'int' en vez de 'str' y 'float' en el peso.
print("EJEMPLO 2: Red de Tuberías (Flujo)")
red_tuberias = Grafo(dirigido=True) # True = El agua solo va en una dirección

red_tuberias.agregar_vertice(1)
red_tuberias.agregar_vertice(2)
red_tuberias.agregar_vertice(3)

red_tuberias.agregar_arista(1, 2, 50.5) # Del nodo 1 al 2, capacidad 50.5
red_tuberias.agregar_arista(2, 3, 20.0) # Del nodo 2 al 3, capacidad 20.0
# Nota: El nodo 3 no conecta a nadie.

red_tuberias.imprimir_grafo()