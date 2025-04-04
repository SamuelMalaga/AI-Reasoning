from grid import Grid
from node import Node
import itertools
import pandas as pd

def basicDFS(grid:Grid, avaliable_words:list):
    avaliable_positions = grid.get_avaliable_positions_on_grid()
    df_avaliable_words = pd.DataFrame(avaliable_words, columns=['words'])
    used_words = []
    explored_nodes = []
    unexplored_nodes = []
    # print("grid positions")
    # print(avaliable_positions)
    # print("passed words")
    # print(df_avaliable_words)
    # print("\n")
    starting_node = Node(None,None)
    execution_stack = [starting_node]

    print(f"Initial execution stack -> {execution_stack}")

    #Initialize the first layer of possible nodes
    for element in itertools.product(avaliable_words, avaliable_positions):
        word, position = element
        # print(f"Node created | w = {word}, pos = {position}")
        new_node_to_explore = Node(word, position)
        unexplored_nodes.append(new_node_to_explore)
        # execution_stack.append(new_node_to_explore)
    
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

    
    # Uses the first node as the initial current node
    # current_node = unexplored_nodes.pop(0)
    

    # # Traverse all nodes in the unexplored nodes list
    # while len(unexplored_nodes) !=0:
    #     # print("UNEXPLORED NODES",unexplored_nodes)
    #     print(f"Execution stack -> {execution_stack}")
    #     print(f"Iterating node -> |{current_node.word}| in position ->|{current_node.position}| at layer -> |{current_layer}| ")
    #     print(f"Removing position {current_node.position} from the list of availiable positions")
    #     avaliable_positions.remove(current_node.position)
    #     print(f"avaliable_positions positions -> {avaliable_positions}")

    #     print(f"Adding word {current_node.word} to used words list")
    #     used_words.append(current_node.word)
    #     print("Used words", used_words)
    #     print("Availiable words: ", df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist())
    #     # print("Availiable positions: ", avaliable_positions)
    #     new_nodes = [Node(word, position, parent=current_node) for word,position in itertools.product(df_avaliable_words[~df_avaliable_words['words'].isin(used_words)]['words'].tolist(),avaliable_positions)]
    #     print(f"New nodes generated: {len(new_nodes)}")
    #     print("Adding new nodes to unexplored nodes")
    #     unexplored_nodes = new_nodes + unexplored_nodes
        
    #     # print("unexplored nodes",unexplored_nodes)
    #     # Get the next node from the unexplored nodes list
    #     next_node = unexplored_nodes.pop(0)
    #     # print("Next node->", next_node)
    #     # next_node.parent = current_node
    #     # Add current node to explored list
    #     explored_nodes.append(current_node)
    #     grid.addWordToGrid(current_node)
    #     # Assign the current node to the next node
    #     current_node = next_node
    #     # Increase layer counter if the layer is not the final one, check condition if is
    #     if current_layer < grid.grid_size:
    #         current_layer=current_layer+1
    #     else:
    #         print(f"at layer {current_layer}, the stopping condition should be checked")
    #         print("is grid solved?:",grid.check_stopping_condition())
    #         if(grid.check_stopping_condition()):
    #             print(f"Found a solution: {current_node} ")
    #             break
    #         else:
    #             # print("Did not found a solution, going back to the root node")
    #             # print("clearing used words")
    #             # used_words = []
    #             # print("clearing avaliable positions")
    #             # avaliable_positions = grid.get_avaliable_positions_on_grid()
    #             # print("Reset layer")
    #             # current_layer = 1
    #             # ## Check if this is the best strategy
    #             # print("reassigning current node")
    #             # current_node = unexplored_nodes.pop(0)
    #             # print("clearing grid")
    #             # print(grid.clear_grid())
    #             print(unexplored_nodes)
    #             break
    #     print("\n")