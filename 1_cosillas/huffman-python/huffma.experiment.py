# ...existing code...
class Nodo:
    """Nodo para árbol de Huffman."""
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def es_hoja(self):
        return self.left is None and self.right is None

def construir_tabla_frecuencias(texto):
    frec = {}
    for c in texto:
        frec[c] = frec.get(c, 0) + 1
    return frec

def construir_arbol(frec):
    if not frec:
        return None
    # lista de tuplas (freq, id, nodo) - id para desempate estable
    lista = []
    _id = 0
    for ch, f in frec.items():
        lista.append((f, _id, Nodo(ch, f)))
        _id += 1

    if len(lista) == 1:
        return lista[0][2]

    # combinar nodos por frecuencia usando ordenación simple
    while len(lista) > 1:
        lista.sort(key=lambda x: (x[0], x[1]))
        f1, id1, n1 = lista.pop(0)
        f2, id2, n2 = lista.pop(0)
        merged = Nodo(None, f1 + f2, left=n1, right=n2)
        lista.append((merged.freq, _id, merged))
        _id += 1

    return lista[0][2]

def construir_codigos(raiz):
    codigos = {}
    if raiz is None:
        return codigos
    def dfs(nodo, pref):
        if nodo.es_hoja():
            codigos[nodo.char] = pref if pref != "" else "0"
            return
        if nodo.left:
            dfs(nodo.left, pref + "0")
        if nodo.right:
            dfs(nodo.right, pref + "1")
    dfs(raiz, "")
    return codigos

def codificar_huffman(frase):
    """
    Codifica 'frase' con Huffman y devuelve la cadena de bits.
    No requiere importaciones en la cabecera del archivo.
    """
    if frase == "":
        return ""
    frec = construir_tabla_frecuencias(frase)
    raiz = construir_arbol(frec)
    codigos = construir_codigos(raiz)
    return "".join(codigos[c] for c in frase)

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    codificado = codificar_huffman(frase)
    print("Frase codificada:", codificado)
# ...existing code...