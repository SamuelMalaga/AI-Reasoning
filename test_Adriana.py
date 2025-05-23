from grid import *
from node_BFS import *
from algorithm_bfs import *
import pandas as pd
import time  

# Define el grid de prueba
test_grid_input = {
    1: [("A", 3, {1: "1D(1)"}), ("d", 3, {1: "1A(1)", 3: "2A(1)"})],
    2: [("A", 4, {1: "1D(3)"})]
}

#3 words
grid1 = {
    1: [("A", 3, {2: "2D(1)"})],
    2: [("D", 3, {1: "1A(2)"})],
    3: [("A", 4, {2: "2D(2)"})],
}

#5 words
grid2 = {
    1: [("A", 4, {1: "2D(1)", 3: "3D(1)"})],
    2: [("D", 4, {1: "1A(1)", 3: "4A(2)"})],
    3: [("D", 3, {1: "1A(3)"})],
    4: [("A", 3, {2: "2D(3)"})],
    5: [("D", 3, {1: "4A(2)"})],
}

#7 words
grid3 = {
    1: [("A", 5, {2: "2D(1)", 4: "3D(1)"})],
    2: [("D", 4, {1: "1A(2)", 3: "4A(1)"})],
    3: [("D", 3, {1: "1A(4)", 2: "5A(2)"})],
    4: [("A", 3, {1: "2D(3)"})],
    5: [("A", 4, {2: "3D(2)"})],
    6: [("D", 3, {1: "5A(3)"})],
    7: [("A", 3, {2: "6D(2)"})],
}

#10 words
grid4 = {
    1: [("A", 5, {1: "2D(1)", 3: "3D(1)", 5: "4D(1)"})],
    2: [("D", 5, {1: "1A(1)", 3: "5A(1)"})],
    3: [("D", 4, {1: "1A(3)", 2: "6A(2)"})],
    4: [("D", 4, {1: "1A(5)", 2: "7A(3)"})],
    5: [("A", 4, {2: "2D(3)", 3: "6D(2)"})],
    6: [("A", 4, {2: "3D(2)"})],
    7: [("A", 5, {3: "4D(2)"})],
    8: [("D", 3, {1: "5A(2)"})],
    9: [("D", 4, {2: "6A(3)"})],
    10:[("A", 3, {2: "9D(2)"})]
}

#12 words
grid5 = {
    1: [("A", 6, {2: "2D(1)", 4: "3D(1)", 6: "4D(1)"})],
    2: [("D", 6, {1: "1A(2)", 3: "5A(1)", 5: "6A(3)"})],
    3: [("D", 5, {1: "1A(4)", 2: "7A(2)"})],
    4: [("D", 5, {1: "1A(6)", 2: "8A(3)"})],
    5: [("A", 4, {2: "2D(3)"})],
    6: [("A", 5, {3: "2D(5)"})],
    7: [("A", 3, {2: "3D(2)"})],
    8: [("A", 4, {2: "4D(3)"})],
    9: [("D", 3, {1: "5A(2)"})],
    10: [("D", 4, {2: "6A(3)"})],
    11: [("D", 5, {1: "7A(1)", 2: "8A(2)"})],
    12: [("A", 4, {2: "11D(2)"})]
}

# Palabras que sabemos que pueden resolver el grid correctamente
#test_words = ["DAD", "DID", "DOME"]

# Leer las palabras desde el archivo 'words_small.txt'
with open('dictionary_small.txt', 'r') as f:
    test_words = [line.strip() for line in f.readlines()]

# Mostrar las palabras cargadas (opcional)
#print("Words loaded from 'dictionary_very_small.txt':")
#print(test_words)

# Crear el grid
test_grid = Grid(grid2)

# Medir el tiempo de ejecución de BFS
start_time = time.time()  # Guardamos el tiempo antes de ejecutar BFS

# Ejecutar BFS con las palabras de prueba
print("----- Running BFS Test -----")
basicBFS(test_grid, test_words)

end_time = time.time()  # Guardamos el tiempo después de ejecutar BFS
elapsed_time = end_time - start_time  # Calculamos el tiempo transcurrido

# Mostrar el tiempo que tardó en encontrar la solución
print(f"\nTime taken to find the solution: {elapsed_time:.4f} seconds")

# Mostrar la solución encontrada por BFS
print("\n----- Grid result from BFS -----")
for key, val in test_grid.generated_grid.items():
    print(f"{key}: {val['word']}")

#  Validación manual forzada
'''
print("\n----- Manual grid injection test -----")
starting_node = Node(None, None)
node_1 = Node("DAD", "1A", parent=starting_node)
node_2 = Node("DID", "1D", parent=node_1)
node_3 = Node("DOME", "2A", parent=node_2)


# Creamos un nuevo grid para no pisar el anterior
manual_test_grid = Grid(test_grid_input)
manual_test_grid.addWordToGrid(node_1)
manual_test_grid.addWordToGrid(node_2)
manual_test_grid.addWordToGrid(node_3)

# Mostrar el grid manual
for key, val in manual_test_grid.generated_grid.items():
    print(f"{key}: {val['word']}")

# Validar si ese camino resuelve correctamente
if manual_test_grid.check_solving(node_3):
    print("\n Manual injection test PASSED (check_solving returned True)")
else:
    print("\n Manual injection test FAILED (check_solving returned False)")

# Validación automática de que BFS encontró la solución correcta
expected_solution = {
    "1A": "DAD",
    "1D": "DID",
    "2A": "DOME"
}
'''

actual_solution = {k: v['word'] for k, v in test_grid.generated_grid.items()}
'''
if actual_solution == expected_solution:
    print("\nBFS found the correct solution!")
else:
    print("\n BFS did NOT find the expected solution.")
    print("Expected:", expected_solution)
    print("Got:", actual_solution)
'''
'''
from grid import *
from node import *
from bfs import *
import pandas as pd

# Define el grid de prueba
test_grid_input = {
    1: [("A", 3, {1: "1D(1)"}), ("d", 3, {1: "1A(1)", 3: "2A(1)"})],
    2: [("A", 4, {1: "1D(3)"})]
}

# Palabras que sabemos que pueden resolver el grid correctamente
test_words = ["DAD", "DID", "DOME"]

# Crear el grid
test_grid = Grid(test_grid_input)

# Ejecutar BFS con las palabras de prueba
print("----- Running BFS Test -----")
basicBFS(test_grid, test_words)

# Mostrar la solución encontrada por BFS
print("\n----- Grid result from BFS -----")
for key, val in test_grid.generated_grid.items():
    print(f"{key}: {val['word']}")

#  Validación manual forzada
print("\n----- Manual grid injection test -----")
starting_node = Node(None, None)
node_1 = Node("DAD", "1A", parent=starting_node)
node_2 = Node("DID", "1D", parent=node_1)
node_3 = Node("DOME", "2A", parent=node_2)

# Creamos un nuevo grid para no pisar el anterior
manual_test_grid = Grid(test_grid_input)
manual_test_grid.addWordToGrid(node_1)
manual_test_grid.addWordToGrid(node_2)
manual_test_grid.addWordToGrid(node_3)

# Mostrar el grid manual
for key, val in manual_test_grid.generated_grid.items():
    print(f"{key}: {val['word']}")

# Validar si ese camino resuelve correctamente
if manual_test_grid.check_solving(node_3):
    print("\n Manual injection test PASSED (check_solving returned True)")
else:
    print("\n Manual injection test FAILED (check_solving returned False)")

# Validación automática de que BFS encontró la solución correcta
expected_solution = {
    "1A": "DAD",
    "1D": "DID",
    "2A": "DOME"
}

actual_solution = {k: v['word'] for k, v in test_grid.generated_grid.items()}

if actual_solution == expected_solution:
    print("\nBFS found the correct solution!")
else:
    print("\n BFS did NOT find the expected solution.")
    print("Expected:", expected_solution)
    print("Got:", actual_solution)
'''




#In case I want to use the word_grid.py library:
'''
from grid import *
from node import *
from bfs import *
import pandas as pd
import time

# Define el grid de prueba
test_grid_input = {
    1: [("A", 3, {1: "1D(1)"}), ("d", 3, {1: "1A(1)", 3: "2A(1)"})],
    2: [("A", 4, {1: "1D(3)"})]
}

# Leer las palabras desde el archivo 'words_small.txt'
with open('words_small.txt', 'r') as f:
    test_words = [line.strip() for line in f.readlines()]

# Mostrar las palabras cargadas (opcional)
print("Words loaded from 'words_small.txt':")
print(test_words)

# Crear el grid
test_grid = Grid(test_grid_input)

# Medir el tiempo de ejecución de BFS
start_time = time.time()  # Guardamos el tiempo antes de ejecutar BFS

# Ejecutar BFS con las palabras de prueba
print("----- Running BFS Test -----")
basicBFS(test_grid, test_words)

end_time = time.time()  # Guardamos el tiempo después de ejecutar BFS
elapsed_time = end_time - start_time  # Calculamos el tiempo transcurrido

# Mostrar el tiempo que tardó en encontrar la solución
print(f"\nTime taken to find the solution: {elapsed_time:.4f} seconds")

# Mostrar la solución encontrada por BFS
print("\n----- Grid result from BFS -----")
for key, val in test_grid.generated_grid.items():
    print(f"{key}: {val['word']}")

#  Validación manual forzada
print("\n----- Manual grid injection test -----")
starting_node = Node(None, None)
node_1 = Node("DAD", "1A", parent=starting_node)
node_2 = Node("DID", "1D", parent=node_1)
node_3 = Node("DOME", "2A", parent=node_2)

# Creamos un nuevo grid para no pisar el anterior
manual_test_grid = Grid(test_grid_input)
manual_test_grid.addWordToGrid(node_1)
manual_test_grid.addWordToGrid(node_2)
manual_test_grid.addWordToGrid(node_3)

# Mostrar el grid manual
for key, val in manual_test_grid.generated_grid.items():
    print(f"{key}: {val['word']}")

# Validar si ese camino resuelve correctamente
if manual_test_grid.check_solving(node_3):
    print("\n Manual injection test PASSED (check_solving returned True)")
else:
    print("\n Manual injection test FAILED (check_solving returned False)")

# Validación automática de que BFS encontró la solución correcta
expected_solution = {
    "1A": "DAD",
    "1D": "DID",
    "2A": "DOME"
}

actual_solution = {k: v['word'] for k, v in test_grid.generated_grid.items()}

if actual_solution == expected_solution:
    print("\nBFS found the correct solution!")
else:
    print("\n BFS did NOT find the expected solution.")
    print("Expected:", expected_solution)
    print("Got:", actual_solution)

'''