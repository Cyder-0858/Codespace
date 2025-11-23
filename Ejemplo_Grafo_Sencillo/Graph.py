class grafffo:
    def __init__(self):
        self.grafffo_dict = {}
    
    def agregar_nodo(self, nodo):
        if nodo in self.grafffo_dict:
            print(f"El nodo {nodo} ya existe.")
        else: 
            self.grafffo_dict[nodo] = []
            print(f"Nodo {nodo} agregado.")
            
    def agregar_arista(self, origen, destino):
        if origen not in self.grafffo_dict:
            print(f"El nodo origen {origen} no existe.")
            return
        if destino not in self.grafffo_dict:
            print(f"El nodo destino {destino} no existe.")
            return
        self.grafffo_dict[origen].append(destino)
        print(f"Arista agregada de {origen} a {destino}.")

    