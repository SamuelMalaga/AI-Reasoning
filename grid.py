from node import Node
import re

class Grid:

    generated_grid: dict[Node]
    grid_size: int
    word_conditions: dict

    def __init__(self,grid_input : dict[tuple]):
        self.grid_input = grid_input 
        self.generated_grid, self.word_conditions = self.generate_grid()
        self.grid_size = self.generated_grid.__len__()

    def __str__(self):
        return f"the grid has a size of {self.grid_size}"
    
    def addNodeToGrid(self,node : Node):
        added_node_position = node.position
        node_at_position = self.generated_grid[added_node_position]
        if node_at_position is None:
            self.generated_grid[added_node_position] = node
        else:
            raise ValueError("The position is already filled with a value")

    def generate_grid(self):
        """
            Funtion to generate the grid that will be filled,
            for now, keys can have any value but try to keep the following:
            N = ["D1","D2"]
                -> N is the number of the word
                -> D1, D2 are the direction of the words, accepted values are A or D (accross or down)
            Input:
                - input_grid : dictionary that follows the convention mentioned below
            
        """
        created_grid = {}
        word_conditions = {}
        for k,v in self.grid_input.items():
            for input_info in v:
                ##Unpack the input info tuple
                (input_direction, input_lenght, position_limitations) = input_info
                ##Create a key in the generated grid dictionary combining the word number and the direction with the initial value of None
                generated_grid_key_name = f"{k}" + input_direction.upper()
                created_grid[f"{generated_grid_key_name}"] = None
                ##Create a key in the word_conditions dictionary with the inputted limitations
                word_conditions[f"{generated_grid_key_name}"] = {
                    "lenght":input_lenght,
                    "cross_positions":position_limitations
                    }
        return created_grid, word_conditions
    
    def check_stopping_condition(self):
        """"
            Check if any of the conditions specified for the grid are violated by the values on it
            - Return:
                True 
                    if there is no constraint violation
                False
                    if there is constraint violation
        """
        for k, v in self.word_conditions.items():
            placed_word_node = self.generated_grid[k]
            word_conditions = v
            ##DEBUG
            # print(f"checking the following word restrictions: |{placed_word_node.word}| at position |{k}|")
            ##Check lenght condition
            if len(placed_word_node.word) != word_conditions["lenght"]:
                return False
                # raise ValueError(f"The lenght of the word in the position -> |{k}| was expected to be |{word_conditions["lenght"]}| .The obtained value was {len(placed_word_node.word)} from the word {placed_word_node.word}")
            
            ##Check crossing position constraints
            for char_position, cross_at_value in word_conditions["cross_positions"].items():
                ##Extractors from the cross at value element

                ####Extract the corresponding match word position
                word_to_match_position = self._extract_word_grid_position(cross_at_value)

                ####Extract the corresponding matching word charachter position
                char_pos = self._extract_word_grid_char_position(cross_at_value)
                
                #DEBUG
                # print(f"\t cross: {k}({char_position}) = {cross_at_value}")
                # print(f"\t word_to_match_position = {word_to_match_position} | word_to_match_char_position = {char_pos}")
                # print(f"\t comparing {k}({char_position}) = {placed_word_node.word.upper()[char_position-1]} to {cross_at_value} = {self.generated_grid[word_to_match_position].word[char_pos]}")
                if placed_word_node.word.upper()[char_position-1] == self.generated_grid[word_to_match_position].word.upper()[char_pos]:
                    #Debug
                    # print("\t they match")
                    return True
                else:
                    #Debug
                    # print("\t they dont match")
                    return False
                # print("\b") 

    def _extract_word_grid_char_position(self, position_string) -> str:
        """
            - Input:
                position_string: str -> formatted string that contains a word position on a grid
            - Output:
                char_position_in_word: int -> A string that specifies the position of a char in a word
        """
        re_word_to_match_char_position = re.search(r"(?<=\()\d+(?=\))",position_string)
        str_char_position_in_word = re_word_to_match_char_position.group(0)
        char_position_in_word = int(str_char_position_in_word) - 1
        return char_position_in_word
    
    def _extract_word_grid_position(self,position_string) -> str:
        """
            - Input:
                position_string: str -> formatted string that contains a word position on a grid
            - Output:
                word_position_in_grid: str -> A string that specifies a key of the generated grid dictionary
        """
        re_word_to_match_position = re.search(r"^[A-Za-z0-9]+",position_string)
        word_position_in_grid = re_word_to_match_position.group(0)

        return word_position_in_grid
    
    def get_avaliable_positions_on_grid(self):
        return list(self.generated_grid.keys())

            

    def __str__(self):
        for k,v in self.generated_grid.items():
            print(f"for position {k}, word {v}")
        return""
