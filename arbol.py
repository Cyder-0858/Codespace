# python
class Nodo:
    """Nodo para árbol n-ario."""
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def añadir_hijo(self, nodo):
        """Añade un Nodo (objeto) como hijo."""
        self.hijos.append(nodo)

    def eliminar_hijo(self, nodo):
        self.hijos = [h for h in self.hijos if h is not nodo]


class ArbolNario:
    """Árbol n-ario con métodos básicos."""
    def __init__(self, raiz: Nodo):
        self.raiz = raiz

    def recorrido_preorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        yield nodo.valor
        for h in nodo.hijos:
            yield from self.recorrido_preorden(h)

    def recorrido_postorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        for h in nodo.hijos:
            yield from self.recorrido_postorden(h)
        yield nodo.valor

    def recorrido_bfs(self):
        from collections import deque
        q = deque([self.raiz])
        while q:
            n = q.popleft()
            yield n.valor
            q.extend(n.hijos)

    def encontrar(self, condicion, nodo=None):
        """Devuelve el primer nodo cuyo valor satisface 'condicion' (función)."""
        if nodo is None:
            nodo = self.raiz
        if condicion(nodo.valor):
            return nodo
        for h in nodo.hijos:
            res = self.encontrar(condicion, h)
            if res:
                return res
        return None

    def tamaño(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        total = 1
        for h in nodo.hijos:
            total += self.tamaño(h)
        return total

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(h) for h in nodo.hijos)

    def imprimir(self, nodo=None, prefijo=""):
        """Imprime el árbol de forma indentada."""
        if nodo is None:
            nodo = self.raiz
        print(f"{prefijo}{nodo.valor}")
        for h in nodo.hijos:
            self.imprimir(h, prefijo + "  ")


if __name__ == "__main__":
    # Ejemplo de uso
    root = Nodo("A")
    b = Nodo("B"); c = Nodo("C"); d = Nodo("D")
    root.añadir_hijo(b); root.añadir_hijo(c); root.añadir_hijo(d)

    b.añadir_hijo(Nodo("B1")); b.añadir_hijo(Nodo("B2"))
    c.añadir_hijo(Nodo("C1"))
    d.añadir_hijo(Nodo("D1")); d.añadir_hijo(Nodo("D2")); d.añadir_hijo(Nodo("D3"))

    arbol = ArbolNario(root)

    print("Impresión del árbol:")
    arbol.imprimir()

    print("\nPreorden:", list(arbol.recorrido_preorden()))
    print("Postorden:", list(arbol.recorrido_postorden()))
    print("BFS:", list(arbol.recorrido_bfs()))
    print("Tamaño:", arbol.tamaño())
    print("Altura:", arbol.altura())

    nodo_c1 = arbol.encontrar(lambda v: v == "C1")
    print("Encontrado:", nodo_c1.valor if nodo_c1 else None)