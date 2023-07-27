# this code was genaret by chatGPT
def printTree(tree):
    for key in tree:
        print(key, end=" ")
        try:
            for value in tree[key]:
                print("->", value, end=" ")
        except:
            print(tree[key], end=" ")
        print()

# An undirected graph is a graph where edges have no direction,
# meaning they represent a symmetric relationship between nodes.

undirected_graph = {
    'A': ['B','C'],
    'B': ['A','C'], 
    'C': {'A','B'}
}

printTree(undirected_graph)

# for item, dir in undirected_graph.items():
#     print(item,'->', dir)

print('*' * 60)
#************************************************************************#

# Directed Graph (Digraph):
# A directed graph is a graph where edges have a direction, indicating a one-way relationship between nodes.

directed_graph = {
    'A' : ['B','D'],
    'B' : ['C'],
    'C' : ['D'],
    'D' : ['A','C']
}

printTree(directed_graph)

# for item, dir in directed_graph.items():
#     print(item, '->', dir)

print('*' * 60)
#************************************************************************#
# Weighted Graph:
# A weighted graph is a graph where each edge has an associated numerical value, called a weight.
weighted_grap = {
    'A' : {'B': 2, 'C':3},
    'B' : {'A': 2, 'C':1},
    'C' : {'A': 3, 'B':1}
}

# printTree(weighted_grap)


for item, dir in weighted_grap.items():
    for v, k in dir.items():
        print(item, '->',v, '->', k)

print('*' * 60)
#************************************************************************#
# Complete Graph:
# A complete graph is a graph in which every pair of distinct nodes is connected by a unique edge.

complete_graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C']
}

# for item, dir in complete_graph.items():
#     print(item, '->', dir)

printTree(complete_graph)

print('*' * 60)
#************************************************************************#
# Tree:
# A tree is a special type of undirected graph without cycles, where there is a unique path between any pair of nodes.

# Tree represented using a dictionary of lists
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
printTree(tree)

print('*' * 60)
#************************************************************************#

# Undirected Graph:

class UndirectedGraph:
    def __init__(self) -> None:
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    
    def print_graph(self):
        for node, nieghbors in self.graph.items():
            print(f'{node}: {" -> ".join([str(_) for _ in nieghbors])}')

undirected_graph = UndirectedGraph()
undirected_graph.add_edge('A', 'B')
undirected_graph.add_edge('A', 'C')
undirected_graph.add_edge('B', 'D')
undirected_graph.print_graph()

print('*' * 60)
#************************************************************************#
    
# Directed Graph (Digraph):

class DirectGraph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_arc(self, startNode, endNode):
        # Add nodes to the graph first
        self.add_node(startNode)
        self.add_node(endNode)
        # Then create an arc from Start Node --> End Node
        self.graph[startNode].append(endNode)
    
    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f'{node}: {" -> ".join([str(_) for _ in neighbors])}')

directed_graph = DirectGraph()
directed_graph.add_arc("A", "B")
directed_graph.add_arc("A", "D")
directed_graph.add_arc("B", "C")
directed_graph.add_arc("C", "D")
directed_graph.print_graph()

print('*' * 60)
#************************************************************************#
# Weighted Graph:

class WeightGraph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_node(self, node):
        if not node in self.graph:
            self.graph[node] = {}

    def add_edge(self, fromNode, toNode, weight):
        self.add_node(fromNode)
        self.add_node(toNode)
        self.graph[fromNode][toNode] = weight
        self.graph[toNode][fromNode] = weight
    
    def print_graph(self):
        # for node, neighbors in self.graph.items():
        #     print(f'{node}: {" -> ".join([str(_) for _ in neighbors])}')
        for item, dir in self.graph.items():
            for v, k in dir.items():
                print(item, '->',v, '->', k)


# Example of a Weighted Graph
weighted_graph = WeightGraph()
weighted_graph.add_edge('A', 'B', 2)
weighted_graph.add_edge('A', 'C', 3)
weighted_graph.print_graph()