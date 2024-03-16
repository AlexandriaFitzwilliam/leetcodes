# Create a Graph class. 
# Graph instances should store all nodes in a graph.
# It should also have an instance method that adds a Node to the graph and a method that connects two existing Node instances together.

class Node:
    """A graph node."""

    def __init__(self, data, adjacent=None):
        self.data = data
        self.adjacent = adjacent or set()

    
    def __repr__(self):
        
        return f'<Node data={self.data} adjacent={self.adjacent}>'
    

    def print_all_adjacent(self):
        """Prints all nodes adjacent to node."""

        for node in self.adjacent:
            print(node)



class Graph:
    """A collection of nodes."""

    def __init__(self, nodes):
        self.nodes = nodes or set()


    def add_node(self, new_node):
        """Adds a new node to the graph collection."""

        self.nodes.add(new_node)


    def connect_nodes(self, node1, node2):
        """Connectes two nodes."""

        node1.adjacent.add(node2)
        node2.adjacent.add(node1)


    def print_all(self):
        """Prints all nodes in graph."""

        for node in self.nodes:
            print(node)



all_nodes = set()

for x in range(5):
    new_node = Node(x)

    all_nodes.add(new_node)

graph1 = Graph(all_nodes)

graph1.print_all()

node5 = Node(5)
node6 = Node(6)

graph1.add_node(node5)
graph1.add_node(node6)
graph1.connect_nodes(node5, node6)

graph1.print_all()
node5.print_all_adjacent()



