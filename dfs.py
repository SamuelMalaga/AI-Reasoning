from grid import Grid
from node import Node
import itertools

def basicDFS(grid:Grid, avaliable_words:dict):
    avaliable_positions = grid.get_avaliable_positions_on_grid()
    explored_nodes = []
    unexplored_nodes = []
    first_node = Node(None,None)
    print("grid positions")
    print(avaliable_positions)
    print("passed words")
    print(avaliable_words)

    #Initialize the first layer of possible nodes
    for element in itertools.product(avaliable_words, avaliable_positions):
        word, position = element
        new_node_to_explore = Node(word, position)
        unexplored_nodes.append(new_node_to_explore)
    
    print("Initial nodes:")
    print(unexplored_nodes)