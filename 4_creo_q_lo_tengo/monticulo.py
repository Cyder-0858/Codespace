class MinHeap:
    """
    TDA: Montículo binario mínimo
    - No usa librerías externas
    - Implementado desde cero
    - Orientado a POO y totalmente reutilizable
    """

    def __init__(self):
        # Representación interna como arreglo
        self._heap = []

    # ---------------------------------------------------------
    # Métodos utilitarios
    # ---------------------------------------------------------
    def is_empty(self):
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)

    def peek(self):
        """Devuelve el mínimo sin extraerlo."""
        return self._heap[0] if not self.is_empty() else None

    # ---------------------------------------------------------
    # Inserción
    # ---------------------------------------------------------
    def push(self, item):
        """
        Inserta un elemento en el montículo.
        El objeto debe soportar comparaciones con <.
        """
        self._heap.append(item)
        self._float_up(len(self._heap) - 1)

    # ---------------------------------------------------------
    # Extracción del mínimo
    # ---------------------------------------------------------
    def pop(self):
        """
        Extrae y devuelve el elemento mínimo del montículo.
        """
        if self.is_empty():
            return None

        min_value = self._heap[0]
        last = self._heap.pop()

        if not self.is_empty():
            self._heap[0] = last
            self._sink_down(0)

        return min_value

    # ---------------------------------------------------------
    # Métodos privados de ordenamiento
    # ---------------------------------------------------------
    def _float_up(self, index):
        """Burbujeo hacia arriba (si el hijo < padre)."""
        parent = (index - 1) // 2

        if index > 0 and self._heap[index] < self._heap[parent]:
            self._swap(index, parent)
            self._float_up(parent)

    def _sink_down(self, index):
        """Hundir el nodo si es mayor que alguno de sus hijos."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self._heap)

        if left < size and self._heap[left] < self._heap[smallest]:
            smallest = left
        if right < size and self._heap[right] < self._heap[smallest]:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._sink_down(smallest)

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]


# --------------------------------------------------------------------
# Ejemplo de uso con una clase TDA que define su propia comparación
# --------------------------------------------------------------------
class Elemento:
    """TDA simple para probar el heap."""
    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, other):
        return self.valor < other.valor

    def __repr__(self):
        return f"Elemento({self.valor})"


# --------------------------------------------------------------------
# Prueba manual
# --------------------------------------------------------------------
if __name__ == "__main__":
    h = MinHeap()

    h.push(Elemento(5))
    h.push(Elemento(3))
    h.push(Elemento(17))
    h.push(Elemento(1))
    h.push(Elemento(9))

    print("Heap inicial:")
    print(h._heap)

    print("\nExtrayendo en orden:")
    while not h.is_empty():
        print(h.pop())
