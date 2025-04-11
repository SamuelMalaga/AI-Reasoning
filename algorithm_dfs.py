from grid import Grid
from node_DFS import Node
import itertools
import pandas as pd
import time
import sys
import datetime

def basicDFS(grid:Grid, avaliable_words:list):
    avaliable_positions = grid.get_avaliable_positions_on_grid()
    df_avaliable_words = pd.DataFrame(avaliable_words, columns=['words'])
    used_words = []
    starting_node = Node(None,None,starting_node=True)
    execution_stack = [starting_node]

    # print(f"Initial execution stack -> {execution_stack}")
    
    current_layer = 0
    current_node = starting_node
    count = 0


    while len(execution_stack) != 0:
        count +=1
        ##Expand the children of the first node
        # print(f"Iterating node -> |{current_node.word}| in position ->|{current_node.position}| at layer -> |{current_node.layer}| ")
        
        if current_node.layer != 0:
            avaliable_positions.remove(current_node.position)
            used_words.append(current_node.word)

        # print(f"avaliable_positions -> {avaliable_positions}")
        # print("Availiable words: ", df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist())
        filtered_words = df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist()
        possible_children = [
            Node(
                word, 
                position, 
                parent=current_node,
                positions_snapshot= avaliable_positions[:],
                used_words_snapshot= used_words[:],
                layer=current_node.layer+1
                ) for word,position in 
                itertools.product(
                    filtered_words,avaliable_positions
                    )
            ]
        
        execution_stack.extend(possible_children)
        next_node = execution_stack.pop()

        # print("Next node: ->", next_node)

        if next_node.starting_node:
            # print("Starting node reached, there is no solution")
            break

        avaliable_positions = next_node.positions_snapshot.copy()
        used_words = next_node.used_words_snapshot.copy()

        # print("Current_node LAYER ->", current_node.layer)
        

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
        # print("\n")

def DFS_len_filter(grid:Grid, avaliable_words:list):
    t0 = datetime.datetime.now()
    avaliable_positions = grid.get_avaliable_positions_on_grid()
    df_avaliable_words = pd.DataFrame(avaliable_words, columns=['words'])
    lenght_restrictions_in_grid = grid.lenghts_restrictions_in_grid()
    df_avaliable_words = df_avaliable_words[df_avaliable_words['words'].str.len().isin(lenght_restrictions_in_grid)]
    used_words = []
    starting_node = Node(None,None,starting_node=True)
    execution_stack = [starting_node]

    current_node = starting_node
    count = 0


    while len(execution_stack) != 0:
        count +=1
        ##Expand the children of the first node
        # print(f"Iterating node -> |{current_node.word}| in position ->|{current_node.position}| at layer -> |{current_node.layer}| ")
        filtered_words = df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist()
        if current_node.layer != 0:
            avaliable_positions.remove(current_node.position)
            used_words.append(current_node.word)
            # df['column_name'] = df[df['column_name'].str.len()!=10]
            # filtered_words = df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist()
            copy = df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]
            filtered_words = copy[copy['words'].str.len()==grid.get_lenght_position_restrictions(current_node.position)]['words'].tolist()

        # print(f"avaliable_positions -> {avaliable_positions}")
        # print("Availiable words: ", filtered_words)
        possible_children = [
            Node(
                word, 
                position, 
                parent=current_node,
                positions_snapshot= avaliable_positions[:],
                used_words_snapshot= used_words[:],
                layer=current_node.layer+1
                ) for word,position in 
                itertools.product(
                    filtered_words,avaliable_positions
                    )
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
    print("timediff:",datetime.datetime.now() - t0)


# recursiveDFS(current_node:Node, grid:Grid, nodes_to_explore:list, current_depth:int, words_dictionary:dict, avaliable_positions:list):


def recursiveDFS(current_node:Node, grid:Grid, words:list, used_words:list,positions:list, used_positions:list):
    #Stopping condition
    if current_node.layer == grid.grid_size:
        print(f"Reached a leaf node ->{current_node.layer}|{current_node.position} with word {current_node.word}, used words = {used_words}, used_positions ={used_positions}")
        return True
    if current_node.word is not None:
        used_words.append(current_node.word)
    if current_node.position is not None:
        used_positions.append(current_node.position)
    ## Generate Candidate
    for next_node in lazy_candidate_generation(current_node.layer+1, words, used_words,positions,used_positions):
        if not recursiveDFS(next_node,grid,words,used_words, positions, used_positions):
            print(f"Leaf not reached at layer->{next_node.layer} with word {next_node.word} and position {next_node.position}")
            return False
        



def lazy_candidate_generation(depth:int, words:list,used_words:list, positions:list, used_positions:list):

    filtered_words = [x for x in words if x not in used_words]
    filtered_positions = [x for x in positions if x not in used_positions]

    # print(f"Call on the lazy candidate generation ->filtered_words:{filtered_words} filtered_positions:{filtered_positions}")

    for position in filtered_positions:
        for word in filtered_words:

            next_node = Node(word,position, used_words_snapshot=used_words,layer=depth)

            yield next_node