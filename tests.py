from grid import Grid
from node import Node


test_grid_input = {
    1: [("A",3,{1:"1D(1)"}),("d",3,{1:"1A(1)",3:"2A(1)"})],
    2: [("A",3,{1:"1D(3)"})]
}

# print(test_grid_input)

test_grid = Grid(test_grid_input)

print("-------Generated grid")
print(test_grid.generated_grid)


print("-------Grid total size")
print(test_grid.grid_size)

## Test for adding nodes
# node_1 = Node(None, "Teste", "2A")
# node_2 = Node(None, "Outro teste", "2A")

# test_grid.addNodeToGrid(node_1)
# test_grid.addNodeToGrid(node_2)

# print("-------Generated grid")
# print(test_grid.generated_grid)

node_1 = Node("Dog", "1A")
node_2 = Node("Dad", "1D")
node_3 = Node("Day", "2A")

test_grid.addNodeToGrid(node_1)
test_grid.addNodeToGrid(node_2)
test_grid.addNodeToGrid(node_3)

print(test_grid.__str__())
print(test_grid.word_conditions)

test_grid.check_stopping_condition()