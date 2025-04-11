from grid import Grid
from node_DFS import Node
from algorithm_dfs import basicDFS, DFS_len_filter, recursiveDFS
import pandas as pd
from collections import defaultdict


test_grid_input = {
    1: [("A",3,{1:"1D(1)"}),("d",3,{1:"1A(1)",3:"2A(1)"})],
    2: [("A",3,{1:"1D(3)"})]
}

# small_grid = {
#     1:[("A", 3,{1:"1D(1)",3:"2D(1)"}), ("D",3,{1:"1A(3)",3:"5A(3)",5:"7A(1)",7:"10A(1)"})]
#     2:
#     3:
#     4:
#     5:
#     6:
#     7:
#     8:
#     9:
#     10:
#     11:
# }
# test_avaliable_words = ["Dog", "Dad", "Day", "Buy", "Map","Sun"]
# test_avaliable_words = [ "DAD","Abys", "DUD", "DBD","oooo","EEEEE","aaaaa","ZZZZZ","PPPPPPs","aaaaaa","BBBBBB","AAAADASDA"]

with open('words_small.txt', 'r') as f:
    small_dictionary = [line.split(',') for line in f.read().splitlines()]
# print(test_grid_input)

##------------------------Testing with native data structures
# Initialize the dictionary
length_dict = defaultdict(list)

with open('words_small.txt', 'r') as file:
    for line in file:
        word = line.strip()
        if word:  # skip empty lines
            length_dict[len(word)].append(word)

# Convert defaultdict to regular dict (optional)
length_dict = dict(length_dict)

##------------------------Testing with native data structures

test_grid = Grid(test_grid_input)

print("-------Generated grid")
print(test_grid.generated_grid)


print("-------Grid total size")
print(test_grid.grid_size)



#test_grid.check_solving(node_3)
#print("TEST GRID RESULT :",test_grid.check_solving(node_3))
# # node_4 = Node("Dog", "1a")

# test_grid.addWordToGrid(node_1)
# test_grid.addWordToGrid(node_2)
# test_grid.addWordToGrid(node_3)

# print(test_grid.get_lenght_position_restrictions("1A"))
# # print(test_grid.word_conditions)

# print("GRID WITH ADDED WORDS:", test_grid.generated_grid)


# print(test_grid.check_stopping_condition())
## -------------Testing on DFS
# print(f"{node_1==node_4}")
DFS_len_filter(test_grid,small_dictionary)


# print(len(small_dictionary))
# print(type(small_dictionary))
# df = pd.read_csv("words.txt",header=None, names=["word"])

# # Check the first few words
# print(df.head())

# df["length"] = df["word"].str.len()

# length_counts = df["length"].value_counts().sort_index()

# # Display results
# print(length_counts)

# print(test_grid.generated_grid)
# print(test_grid.word_conditions)

# loading()
# print("-------Testing")

# print("produced dictionary")
# for length, words in length_dict.items():
#     print(f"Length {length}: {len(words)}")

# test_avaliable_words = ["Dog", "Dad", "Day", "map", "sun", "buy"]
# root_node = Node(None, None)
# unexplored_nodes = [root_node]
# used_words = []
# used_positions = []
# avaliable_positions = test_grid.get_avaliable_positions_on_grid()
# recursiveDFS(root_node,test_grid,test_avaliable_words,used_words, avaliable_positions, used_positions)


