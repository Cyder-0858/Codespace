G = {"A", "B", "C", "D"}

class ejemplo_grafo_dirigido:
    def __init__(self):
        self.grafo_dict = {}

    def agregar_nodo(self, nodo):
            if nodo not in self.grafo_dict:
                self.grafo_dict = []
                print ("nodo agregado correctamente")
            else:
                 return "nodo ya agregado"
            
    def agregar_arista(self, arista):
                  nodo1 = arista.get_nodo1()
                            nodo2 = arista.get_nodo2()
                                        if nodo1 not in self.grafo_dict:
                                                        print(f"El nodo origen {nodo1} no existe.")
                                                                        return
                                                                                    if nodo2 not in self.grafo_dict:
                                                                                                    print(f"El nodo destino {nodo2} no existe.")
                                                                                                                    return
                                                                                                                                self.grafo_dict[nodo1].append(nodo2)
                                                                                                                                            print(f"Arista agregada de {nodo1} a {nodo2}.")
          

class ejemplo_arista:
    def __init__(self,nodo1, nodo2):
         self.nodo1 = nodo1
         self.nodo2 = nodo2

    def get_nodo1(self):
         return self.nodo1
    def get_nodo2(self):
         return self.nodo2
    
    def __str__(self):
         return f"({self.nodo1.get_nombre} -> {self.nodo2.get_nombre})"
    

class ejemplo_nodo:
     def __init__(self, nombre):
          self.nombre = nombre

    def get_nombre(self):
          return self.nombre

    def __str__(self):
          return f"{self.nombre}"