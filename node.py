class Node:
    
    parent = None

    def __init__(self,word:str, position:str):
        self.word = word
        self.position = position

    def __str__(self):
        return f"This is a node at the position {self.position} with the value {self.word}"

    def __eq__(self, another_node):
        if not isinstance(another_node, Node):
            raise TypeError(f'Cannot compare object of type node with type {type(another_node)}')
        if self.word.upper() == another_node.word.upper() and self.position == another_node.position.upper():
            return True
        else:
            return False 
