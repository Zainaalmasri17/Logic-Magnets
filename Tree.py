class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, child): 
      self.children.append(Node(child))

class Tree:
    def __init__(self, data):
        self.root = Node(data)
    
    # def add_edge(self, parent_node, child_grid):
    #     child_node = Node(child_grid)  # Create a new Node with the child grid
    #     parent_node.add_child(child_node)  # Add the child node to the parent node's children
    #     return child_node

    # def insert_node(self, root, node):
    #     if root is None:
    #         root = node
    #     else:
    #         root.add_child(node)

# node = Node('A')
# node.add_child('B')
# print(node.children)

# tree = Tree('A')
# tree.root.add_child('B')
# tree.root.children[0].add_child('C')
# tree.root.add_child('D')
# print(tree.root.children[1].data)
