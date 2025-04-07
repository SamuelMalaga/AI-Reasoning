from grid import Grid
from node import Node
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

#Returns the recursive call returns true, the algorithm stops, if false, it continues
def recursiveDFS(reference_grid: Grid, node_list, current_depth, words_dictionary):
    #Check stopping condition
    if current_depth == reference_grid.grid_size:
        print("Found solution:", reference_grid)
        return True  # stop after first solution (can be adapted)

    #get lenght constraint
    length = word_lengths[current_depth]
    #Get starting letter constraint
    first_letter = starting_letters[current_depth]

    #Lazy generate candidate
    for candidate in generate_candidates(current_depth, words_dictionary):
        ## check if the current node satisfies the constraint
        if satisfies_constraints(candidate, grid):  # prune early based on leght
            ##Add the node into the node_list
            grid.append(candidate)
            ##Link to the next call on the stack
            if dfs(grid, depth + 1, max_depth, word_lengths, starting_letters):
                return True  # propagate success
            ## Does not return true, backtrack
            grid.pop()  # backtrack

    #bottom line checker
    return False 

def generate_candidates(depth, words_dictionary:dict):
    """Lazy generator that yields words matching constraints"""
    for word in words_dictionary.get(depth):
        yield word

def satisfies_constraints(word, grid):
    """Prune: simple constraint - don't repeat words"""
    return word not in grid

#GPT GENERATED CODE BELOW    

# # A pretend "huge" dictionary
# FAKE_DICTIONARY = [
#     "apple", "angle", "arena", "badge", "baker", "cabin", "camel",
#     "delta", "eagle", "fable", "gamma", "hello", "hotel", "igloo", "joker"
# ]

# def generate_candidates(length, starting_letter):
#     """Lazy generator that yields words matching constraints"""
#     for word in FAKE_DICTIONARY:
#         if len(word) == length and word.startswith(starting_letter):
#             yield word

# def satisfies_constraints(word, grid):
#     """Prune: simple constraint - don't repeat words"""
#     return word not in grid

# def dfs(grid, depth, max_depth, word_lengths, starting_letters):
#     if depth == max_depth:
#         print("Found solution:", grid)
#         return True  # stop after first solution (can be adapted)

#     length = word_lengths[depth]
#     first_letter = starting_letters[depth]

#     for candidate in generate_candidates(length, first_letter):
#         if satisfies_constraints(candidate, grid):  # prune early
#             grid.append(candidate)
#             if dfs(grid, depth + 1, max_depth, word_lengths, starting_letters):
#                 return True  # propagate success
#             grid.pop()  # backtrack

#     return False  # no valid candidate at this depth

# # 🔧 Example usage
# word_lengths = [5, 5, 5]             # each word must be 5 letters
# starting_letters = ['a', 'b', 'c']   # each word must start with a different letter

# dfs(grid=[], depth=0, max_depth=3, word_lengths=word_lengths, starting_letters=starting_letters)
