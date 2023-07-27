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

# Sure! Let's continue with more complex code examples for graphs in Python. We'll now 
# implement breadth-first search (BFS) and depth-first search (DFS) algorithms for traversing the graphs.
# Breadth-First Search (BFS):

class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)

        self.graph[from_node].append(to_node)
        self.graph[to_node].append(from_node)

    def bfs(self, start_node):
        visited = set()
        queue   = [start_node]
        visited.add(start_node)
        
        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")
            for nieghbor in self.graph[current_node]:
                if nieghbor not in visited:
                    queue.append(nieghbor)
                    visited.add(nieghbor)

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f'{node}: {" -> ".join([str(_) for _ in neighbors])}')

graph_bfs = Graph()
graph_bfs.add_edge('A', 'B')
graph_bfs.add_edge('A', 'C')
graph_bfs.add_edge('B', 'D')
graph_bfs.add_edge('C', 'E')
graph_bfs.add_edge('C', 'F')
# printTree(graph_bfs)
graph_bfs.print_graph()
graph_bfs.bfs('B')

print()
print('*' * 60)
#************************************************************************#
# Directed Acyclic Graph (DAG):

class DAG:
    def __init__(self) -> None:
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)

        self.graph[from_node].append(to_node)
    
    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f'{node}: {" -> ".join([str(_) for _ in neighbors])}')

    def topological_sort(self):
        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)

        for node in self.graph:
            if node not in visited:
                dfs(node)

        return stack[::-1]        

dag = DAG()
dag.add_edge('A', 'B')
dag.add_edge('A', 'C')
dag.add_edge('B', 'D')
dag.add_edge('C', 'D')
dag.print_graph()

topological_order = dag.topological_sort()
print(topological_order)

print('*' * 60)
#************************************************************************#
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, node1, node2, weight=None):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self):
        if self.weight is not None:
            return f"{self.node1} --({self.weight})-- {self.node2}"
        return f"{self.node1} -- {self.node2}"

# Undirected graph
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')

edge_ab = Edge(node_a, node_b)
edge_ac = Edge(node_a, node_c)

node_a.add_neighbor(node_b)
node_a.add_neighbor(node_c)
node_b.add_neighbor(node_a)
node_c.add_neighbor(node_a)

print(edge_ab)
print(edge_ac)

print('*' * 60)
#************************************************************************#

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, from_node, to_node, weight=1):
        if from_node >= self.num_nodes or to_node >= self.num_nodes:
            raise ValueError("Node index out of range")

        self.matrix[from_node][to_node] = weight
        self.matrix[to_node][from_node] = weight  # For an undirected graph

    def __str__(self):
        return "\n".join(" ".join(str(val) for val in row) for row in self.matrix)


# Example of an Adjacency Matrix for a weighted graph
graph_matrix = Graph(4)
graph_matrix.add_edge(0, 1, 2)
graph_matrix.add_edge(0, 2, 3)
graph_matrix.add_edge(1, 2, 1)
graph_matrix.add_edge(1, 3, 4)
print(graph_matrix)

print('*' * 60)
#************************************************************************#
class EdgeListGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_edge(self, node1, node2, weight=None):
        if node1 not in self.nodes:
            self.nodes[node1] = Node(node1)
        if node2 not in self.nodes:
            self.nodes[node2] = Node(node2)

        edge = Edge(node1, node2, weight)
        self.edges.append(edge)

        self.nodes[node1].add_neighbor(self.nodes[node2])
        self.nodes[node2].add_neighbor(self.nodes[node1])

    def get_edge_list(self):
        return self.edges

    def __str__(self):
        return "\n".join(str(edge) for edge in self.edges)


# Example of a graph with the Edge List representation
edge_list_graph = EdgeListGraph()
edge_list_graph.add_edge('A', 'B', 2)
edge_list_graph.add_edge('A', 'C', 3)
edge_list_graph.add_edge('B', 'C', 1)
edge_list_graph.add_edge('B', 'D', 6)
edge_list_graph.add_edge('C', 'D', 4)

print("Edge List:")
print(edge_list_graph.get_edge_list())
