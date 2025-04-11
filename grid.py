from node_DFS import Node
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
        
    def addWordToGrid(self,node : Node):
        # print(f"Adding node to position {node.position} with value {node.word}")
        added_node_position = node.position
        word_at_position = self.generated_grid[added_node_position]['word']
        if word_at_position is None:
            self.generated_grid[added_node_position]['word'] = node.word
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
                created_grid[f"{generated_grid_key_name}"] = {
                    "word":None,
                    "lenght":input_lenght,
                    "cross_positions":position_limitations
                    }
                ##Create a key in the word_conditions dictionary with the inputted limitations
                word_conditions[f"{generated_grid_key_name}"] = {
                    "word":None,
                    "lenght":input_lenght,
                    "cross_positions":position_limitations
                    }
        return created_grid, word_conditions
    
    def _generate_node_list_by_node(self, node):
        node_list = []
        current_node = node
        while current_node.word is not None:
            node_list.append(current_node)
            tmp = current_node.parent
            current_node = tmp
        return node_list

    def check_solving(self, node:Node):
        current_node = node
        nodes_list = self._generate_node_list_by_node(node)
        print("Passed nodes list: ", nodes_list)

        ## Check positional constraints and lenght constraing
        while current_node.word is not None:
            current_node_position = current_node.position
            current_node_word = current_node.word
            # print(f"checking the following word restrictions: |{current_node_word}| at position |{current_node_position}|")
            if len(current_node_word) != self.generated_grid[current_node_position]['lenght']:
                return False
            for char_position, cross_at_value in self.generated_grid[current_node_position]['cross_positions'].items():
                ####Extract the corresponding match word position
                word_to_match_position = self._extract_word_grid_position(cross_at_value)

                ####Extract the corresponding matching word charachter position
                char_pos = self._extract_word_grid_char_position(cross_at_value)
                # print(f"\t {word_to_match_position}")
                ### get the word to compare
                for node in nodes_list:
                    if node.position == word_to_match_position:
                        word_to_compare = node.word
                # print(f"\t {word_to_compare}")
                if current_node_word.upper()[char_position-1] != word_to_compare.upper()[char_pos]:
                    #Debug
                    # print("\t they match")
                    return False
            # print(current_node)
            tmp = current_node.parent
            current_node = tmp
            # print("\b")
        return True
    
    def check_stopping_condition(self):
        """"
            Check if any of the conditions specified for the grid are violated by the values on it
            - Return:
                True 
                    if there is no constraint violation
                False
                    if there is constraint violation
        """
        # print("items:", list(self.generated_grid.items()))
        for item in list(self.generated_grid.items()):
            k,v = item
            # print("Key",k)
            # print("value",v)
            placed_word = self.generated_grid[k]['word']
            word_conditions = v
            ##DEBUG
            # print(f"checking the following word restrictions: |{placed_word}| at position |{k}|")
            ##Check lenght condition
            if len(placed_word) != self.generated_grid[k]['lenght']:
                return False
                # raise ValueError(f"The lenght of the word in the position -> |{k}| was expected to be |{word_conditions["lenght"]}| .The obtained value was {len(placed_word)} from the word {placed_word}")
            
            # print("Crossing rules", self.generated_grid[k]['lenght'])
            ##Check crossing position constraints
            for char_position, cross_at_value in self.generated_grid[k]['cross_positions'].items():
                ##Extractors from the cross at value element

                ####Extract the corresponding match word position
                word_to_match_position = self._extract_word_grid_position(cross_at_value)

                ####Extract the corresponding matching word charachter position
                char_pos = self._extract_word_grid_char_position(cross_at_value)
                
                #DEBUG
                # print(f"\t cross: {k}({char_position}) = {cross_at_value}")
                # print(f"\t word_to_match_position = {word_to_match_position} | word_to_match_char_position = {char_pos}")
                # print(f"\t comparing {k}({char_position}) = {placed_word.upper()[char_position-1]} to {cross_at_value} = {self.generated_grid[word_to_match_position].word[char_pos]}")
                if placed_word.upper()[char_position-1] != self.generated_grid[word_to_match_position]['word'].upper()[char_pos]:
                    #Debug
                    # print("\t they match")
                    return False
                # print("\b") 
        return True
    
    def get_lenght_position_restrictions(self, pos_string:str)->str:
        pos_string = pos_string.upper()
        len_restriction = self.generated_grid[pos_string]['lenght']
        return len_restriction
    
    def get_crossing_position_restrictions(self, pos_string:str)->dict:
        pos_string = pos_string.upper()
        crossing_restrictions = self.generated_grid[pos_string]['cross_positions']
        return crossing_restrictions

    def lenghts_restrictions_in_grid(self):
        observed_lenghts=[]
        for position_string, restrictions in self.generated_grid.items():
            lenght_restriction = restrictions['lenght']
            if lenght_restriction not in observed_lenghts:
                observed_lenghts.append(lenght_restriction)
                
        return observed_lenghts

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

    def clear_grid(self):
        for position, value in self.generated_grid.items():
            self.generated_grid[f"{position}"]['word'] = None
            

    def __str__(self):
        for k,v in self.generated_grid.items():
            print(f"for position {k}, word {v}")
        return""
    
    ##Iadded this one for BFS
    # is_valid_placement en grid.py
    def is_valid_placement(self, node: Node):
        if node.word is None:
            return False

        if node.position not in self.generated_grid:
            return False

        expected_length = self.generated_grid[node.position]['lenght']
        if len(node.word) != expected_length:
            return False

        # Check crossing constraints
        cross_constraints = self.generated_grid[node.position]['cross_positions']
        for char_position, cross_at in cross_constraints.items():
            match_pos = self._extract_word_grid_position(cross_at)
            match_index = self._extract_word_grid_char_position(cross_at)
            
            if self.generated_grid.get(match_pos, {}).get('word') is not None:
                match_word = self.generated_grid[match_pos]['word']
                if match_index >= len(match_word) or char_position - 1 >= len(node.word):
                    return False
                if node.word[char_position - 1].upper() != match_word[match_index].upper():
                    return False

        return True