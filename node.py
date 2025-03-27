class Node:
    
    def __init__(self, _depth, _parent, _action, _value):
        self.depth = _depth
        self.parent = _parent
        self.action = _action
        self.value = _value

    def __str__(self):
        return f"This is a node at the position {self.depth} with the value {self.value}"    



# Node1 = Node(None,None,None)
# Node2 = Node(1,Node1, "add")


# print(Node2.depth)