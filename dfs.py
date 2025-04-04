from grid import Grid
from node import Node
import itertools
import pandas as pd

def basicDFS(grid:Grid, avaliable_words:list):
    avaliable_positions = grid.get_avaliable_positions_on_grid()
    df_avaliable_words = pd.DataFrame(avaliable_words, columns=['words'])
    used_words = []
    # explored_nodes = []
    # unexplored_nodes = []
    starting_node = Node(None,None)
    execution_stack = [starting_node]

    print(f"Initial execution stack -> {execution_stack}")

    #Initialize the first layer of possible nodes
    # for element in itertools.product(avaliable_words, avaliable_positions):
    #     word, position = element
    #     # print(f"Node created | w = {word}, pos = {position}")
    #     new_node_to_explore = Node(word, position)
    #     unexplored_nodes.append(new_node_to_explore)
    #     # execution_stack.append(new_node_to_explore)
    
    current_layer = 0
    current_node = starting_node


    while len(execution_stack) != 0:
        ##Expand the children of the first node
        print(f"Iterating node -> |{current_node.word}| in position ->|{current_node.position}| at layer -> |{current_layer}| ")
        
        if current_layer != 0:
            avaliable_positions.remove(current_node.position)
            used_words.append(current_node.word)

        print(f"avaliable_positions -> {avaliable_positions}")
        print("Availiable words: ", df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist())
        possible_children = [
            Node(
                word, 
                position, 
                parent=current_node,
                positions_snapshot= avaliable_positions,
                used_words_snapshot= used_words
                ) for word,position in itertools.product(df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist(),avaliable_positions)
            ]
        
        execution_stack.extend(possible_children)
        print("Exec stack before",len(execution_stack))
        next_node = execution_stack.pop()

        if current_layer < grid.grid_size:
            current_layer=current_layer+1
        else:
            if(grid.check_solving(current_node)):
                print(f"Found a solution: {current_node} ")
                break
            else:
                print(f"Did not found a solution ")
        print(f"next node to be iterated -> {next_node}")

        current_node = next_node
        print("\n")
        

    print(grid)