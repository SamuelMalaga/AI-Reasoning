from grid import Grid
from node import Node
from dfs import basicDFS
import pandas as pd


test_grid_input = {
    1: [("A",3,{1:"1D(1)"}),("d",3,{1:"1A(1)",3:"2A(1)"})],
    2: [("A",3,{1:"1D(3)"})]
}
# test_avaliable_words = ["Dog", "Dad", "Day", "Buy", "Map","Sun"]
test_avaliable_words = [ "Buy", "Dog", "Day", "Dad"]

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
# print(test_grid.generated_grid["1A"]['word'])
starting_node = Node(None,None)
node_1 = Node("Dog", "1A", parent= starting_node)
node_2 = Node("Dad", "1D", parent=node_1)
node_3 = Node("Day", "2A", parent=node_2)

#test_grid.check_solving(node_3)
#print("TEST GRID RESULT :",test_grid.check_solving(node_3))
# # node_4 = Node("Dog", "1a")

# test_grid.addWordToGrid(node_1)
# test_grid.addWordToGrid(node_2)
# test_grid.addWordToGrid(node_3)

# # print(test_grid.__str__())
# # print(test_grid.word_conditions)

# print("GRID WITH ADDED WORDS:", test_grid.generated_grid)


# print(test_grid.check_stopping_condition())
# ## -------------Testing on DFS
# print(f"{node_1==node_4}")
basicDFS(test_grid,test_avaliable_words)

# df = pd.read_csv("words.txt",header=None, names=["word"])

# # Check the first few words
# print(df.head())

# df["length"] = df["word"].str.len()

# length_counts = df["length"].value_counts().sort_index()

# # Display results
# print(length_counts)

# print(test_grid.generated_grid)
# print(test_grid.word_conditions)