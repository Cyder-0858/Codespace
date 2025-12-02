# ============================================================================
# TDA: Node (Nodo del Árbol Binario de Búsqueda)
# ============================================================================
class Node:
    """
    TDA que representa un nodo del Árbol Binario de Búsqueda (BST).
    Guarda un valor y referencias a hijos izquierdo y derecho.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"


# ============================================================================
# TDA: Binary Search Tree (Árbol Binario de Búsqueda)
# ============================================================================
class BST:
    """
    TDA que implementa un Árbol Binario de Búsqueda clásico:
    - Insertar valores
    - Buscar valores
    - Recorridos (in-order, pre-order, post-order)
    - Mínimo, máximo
    - Eliminación de nodos
    No utiliza librerías externas.
    """

    def __init__(self):
        self.root = None

    # ----------------------------------------------------------------------
    # Insertar un valor
    # ----------------------------------------------------------------------
    def insert(self, value):
        """Inserta un valor en el BST manteniendo el orden."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    # ----------------------------------------------------------------------
    # Buscar un valor (aprovechando el orden del árbol)
    # ----------------------------------------------------------------------
    def search(self, value):
        """
        Devuelve True si el valor está en el árbol.
        Aprovecha el orden del BST para podar ramas.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    # ----------------------------------------------------------------------
    # Obtener valor mínimo
    # ----------------------------------------------------------------------
    def min_value(self):
        current = self.root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current.value

    # ----------------------------------------------------------------------
    # Obtener valor máximo
    # ----------------------------------------------------------------------
    def max_value(self):
        current = self.root
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        return current.value

    # ----------------------------------------------------------------------
    # Eliminar un valor del BST
    # ----------------------------------------------------------------------
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Caso 1: Nodo sin hijos
            if current.left is None and current.right is None:
                return None
            # Caso 2: Un solo hijo
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            # Caso 3: Dos hijos → reemplazar por el mínimo del subárbol derecho
            successor = self._min_node(current.right)
            current.value = successor.value
            current.right = self._delete_recursive(current.right, successor.value)

        return current

    def _min_node(self, current):
        while current.left:
            current = current.left
        return current

    # ----------------------------------------------------------------------
    # Recorridos
    # ----------------------------------------------------------------------
    def inorder(self):
        resultado = []
        self._inorder_recursive(self.root, resultado)
        return resultado

    def _inorder_recursive(self, current, resultado):
        if current:
            self._inorder_recursive(current.left, resultado)
            resultado.append(current.value)
            self._inorder_recursive(current.right, resultado)

    def preorder(self):
        resultado = []
        self._pre_recursive(self.root, resultado)
        return resultado

    def _pre_recursive(self, current, resultado):
        if current:
            resultado.append(current.value)
            self._pre_recursive(current.left, resultado)
            self._pre_recursive(current.right, resultado)

    def postorder(self):
        resultado = []
        self._post_recursive(self.root, resultado)
        return resultado

    def _post_recursive(self, current, resultado):
        if current:
            self._post_recursive(current.left, resultado)
            self._post_recursive(current.right, resultado)
            resultado.append(current.value)


# ============================================================================
# EJEMPLO DE USO
# ============================================================================
if __name__ == "__main__":

    bst = BST()

    valores = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for v in valores:
        bst.insert(v)

    print("Árbol (in-order):", bst.inorder())

    print("Buscar 7:", bst.search(7))
    print("Buscar 15:", bst.search(15))

    print("Minimo:", bst.min_value())
    print("Maximo:", bst.max_value())

    bst.delete(3)
    print("Árbol tras eliminar 3 (in-order):", bst.inorder())
