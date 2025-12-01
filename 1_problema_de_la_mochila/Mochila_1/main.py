# -------------------------------------------------------
# PRUEBA COMPLETA — STAR WARS
# -------------------------------------------------------

items = [
    Item("Sable de luz", 5, 90),
    Item("Holoproyector", 2, 40),
    Item("Bláster DL-44", 4, 70),
    Item("Herramientas de reparación", 3, 50),
    Item("Mini-dron de reconocimiento", 6, 85)
]

capacity = 15

# Construcción del grafo
graph = Graph(items, capacity)
graph.build()

# Resolver
solver = KnapsackSolver(graph)
solution, total_priority = solver.solve()

# Imprimir resultados
print("\n===========================")
print("   SOLUCIÓN ÓPTIMA")
print("===========================\n")

for action, item in solution:
    accion = "Tomar" if action == "take" else "Saltar"
    print(f"{accion}: {item}")

print(f"\nPrioridad total lograda: {total_priority}")
print("===========================\n")