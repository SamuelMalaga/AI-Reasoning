from grid import Grid
from node import Node
import itertools
import pandas as pd
import time

def basicDFS(grid:Grid, avaliable_words:list):
    avaliable_positions = grid.get_avaliable_positions_on_grid()
    df_avaliable_words = pd.DataFrame(avaliable_words, columns=['words'])
    used_words = []
    starting_node = Node(None,None,starting_node=True)
    execution_stack = [starting_node]

    print(f"Initial execution stack -> {execution_stack}")
    
    current_layer = 0
    current_node = starting_node
    count = 0


    while len(execution_stack) != 0:
        count +=1
        ##Expand the children of the first node
        print(f"Iterating node -> |{current_node.word}| in position ->|{current_node.position}| at layer -> |{current_node.layer}| ")
        
        if current_node.layer != 0:
            avaliable_positions.remove(current_node.position)
            used_words.append(current_node.word)

        print(f"avaliable_positions -> {avaliable_positions}")
        print("Availiable words: ", df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist())
        possible_children = [
            Node(
                word, 
                position, 
                parent=current_node,
                positions_snapshot= avaliable_positions[:],
                used_words_snapshot= used_words[:],
                layer=current_node.layer+1
                ) for word,position in itertools.product(df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist(),avaliable_positions)
            ]
        
        execution_stack.extend(possible_children)
        next_node = execution_stack.pop()

        print("Next node: ->", next_node)

        if next_node.starting_node:
            print("Starting node reached, there is no solution")
            break

        avaliable_positions = next_node.positions_snapshot.copy()
        used_words = next_node.used_words_snapshot.copy()

        print("Current_node LAYER ->", current_node.layer)
        

        if current_node.layer == grid.grid_size:
            if(grid.check_solving(current_node)):
                print(f"Found a solution: {current_node} ")
                break
            else:
                print(f"Did not found a solution, backtracking to {next_node} at layer {next_node.layer}")
            
        # print(f"next node to be iterated -> {next_node}")

        # time.sleep(2)
        current_node = next_node
        print(f"count -> {count}")
        print("\n")