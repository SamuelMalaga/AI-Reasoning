class Node:
    
    parent = None

    def __init__(self,word, position):
        self.word = word
        self.position = position

    def __str__(self):
        return f"This is a node at the position {self.position} with the value {self.word}"    


