from node import Node

class grid:

    def __init__(self,gridsize):
        self.gridsize = gridsize
        self.gridElements = [None] * gridsize

    def __str__(self):
        return f"the grid has a size of {self.gridsize}"
    
    def addNodeToGrid(self,node : Node):
        node_position = node.depth - 1
        if node.depth > self.gridsize:
            raise ValueError("The depth of the node is bigger than the grid depth")
        if self.gridElements[node_position] is not None:
            raise ValueError("You cannot add a node to a position that is already filled")
        if node_position < 0:
            raise ValueError("Prohibido")
        self.gridElements[node_position] = Node


new_grid = grid(3)
new_node1 = Node(1,None,1,"test1")
new_node2 = Node(2,None,2,"test2")
new_node3 = Node(3,None,3,"test3")
new_node4 = Node(-1,None,-1,"test4")


#print(new_grid)
new_grid.addNodeToGrid(new_node1)
new_grid.addNodeToGrid(new_node2)
new_grid.addNodeToGrid(new_node3)
new_grid.addNodeToGrid(new_node4)


for node in new_grid.gridElements:
    print(node)