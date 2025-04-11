class Node:
    
    parent = None
    ''' I used a copy down here to define that I want to use the copy, so the info is shared between the nodes
    def __init__(self,word:str, position:str, parent = None,positions_snapshot = None,used_words_snapshot = None, layer = 0, starting_node=False):
        self.word = word
        self.position = position
        self.parent = parent
        self.positions_snapshot = positions_snapshot
        self.used_words_snapshot = used_words_snapshot
        self.layer = layer
        self.starting_node = starting_node
    '''

    def __init__(self, word: str, position: str, parent=None,positions_snapshot=None, used_words_snapshot=None,layer=0, starting_node=False):
        self.word = word
        self.position = position
        self.parent = parent
        self.positions_snapshot = positions_snapshot.copy() if positions_snapshot else []
        self.used_words_snapshot = used_words_snapshot.copy() if used_words_snapshot else []
        self.layer = layer
        self.starting_node = starting_node


    def __str__(self):
        return f"{self.position}={self.word}"

    def __repr__(self):
        return f"Node(pos:{self.position},word:{self.word})"

    def __eq__(self, another_node):
        if not isinstance(another_node, Node):
            raise TypeError(f'Cannot compare object of type node with type {type(another_node)}')
        if self.word.upper() == another_node.word.upper() and self.position == another_node.position.upper():
            return True
        else:
            return False 