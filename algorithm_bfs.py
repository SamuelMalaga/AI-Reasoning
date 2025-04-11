from grid import Grid
from node_DFS import Node
import itertools
import pandas as pd
import time
from collections import deque

def print_solution_path(node):#this one is just for printing the solution
    path = []
    while node:
        if node.word and node.position:
            path.append(f"{node.position}: {node.word}")
        node = node.parent
    print("Solution path:\n" + "\n".join(reversed(path)))


def basicBFS(grid: Grid, available_words: list):
    available_positions = grid.get_avaliable_positions_on_grid()#posible positions to put words
    df_available_words = pd.DataFrame(available_words, columns=['words'])
    used_words = []

    starting_node = Node(None, None, starting_node=True, layer=0)#defined with nothing inside
    execution_queue = deque([starting_node])#pending nodes

    count = 0

    while execution_queue:
        current_node = execution_queue.popleft() 
        count += 1

        # Here it refreshes the last info about position and words used
        if not current_node.starting_node:
            available_positions = current_node.positions_snapshot[:]
            used_words = current_node.used_words_snapshot[:]
            if current_node.position in available_positions:
                available_positions.remove(current_node.position)
            used_words.append(current_node.word)#if the node is not the initial node, it refreshes everything in father and deletes the actual position from the available positions

        # Here it verifies if the game is already solved
        if len(used_words) == len(grid.generated_grid) and grid.check_stopping_condition():
            print("Solution found!")
            print_solution_path(current_node)
            return current_node

        # Here it filters the available words that has not been used
        filtered_words = df_available_words[~df_available_words['words'].isin(used_words)]['words'].tolist()

        #Here it verifies the lenght
        if current_node.position:
            expected_length = grid.get_lenght_position_restrictions(current_node.position)
            filtered_words = [w for w in filtered_words if len(w) == expected_length]

        possible_children = []
        for position in available_positions:
            expected_length = grid.get_lenght_position_restrictions(position)
            for word in filtered_words:
                if len(word) != expected_length:
                    continue

                test_node = Node(word, position)
                if not grid.is_valid_placement(test_node):
                    continue

                print(f"   Trying word: {word} at position {position}")
                print(f"   -> Used words: {used_words + [word]}")
                print(f"   -> Available positions: {available_positions}")
                print(f"   -> Layer: {current_node.layer + 1}")
                print(f"   -> Expected word length: {expected_length}")

                child = Node(
                    word,
                    position,
                    parent=current_node,
                    positions_snapshot=available_positions[:],
                    used_words_snapshot=used_words[:],
                    layer=current_node.layer + 1
                )

                # Here it verifies if the position is already in use before putting a word
                if grid.generated_grid[position]["word"] is not None:
                    print(f"The position {position} is already occupied")
                    continue  # Here it gets out of the loop and it doesnt add the word to this position

                grid.addWordToGrid(child)

                # After adding the word into the game, it refreshes the positions and the words 
                used_words.append(word)
                available_positions.remove(position)

                possible_children.append(child)

        # Here it adds the posible children nodes to the queue of execution
        execution_queue.extend(possible_children)

    # In case it doesn't find a solution
    deepest_node = current_node  # just to be sure, we refresh this one
    print(" No solution found.")
    print(" Deepest attempt:")
    print_solution_path(deepest_node)
    return None
