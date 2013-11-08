import sys
sys.setrecursionlimit(100000)

# Defines a node, that node's contents, and the neighbors to that node and the
# edge weights to access that neighbor
class Node:

    # Initialize a node, with name containing the contents of the node,
    # and neighbors being a dictionary containing the neighbor's name as the 
    # key and the weight of the edge between them as the value
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.visited = False

    # Accessor for the name
    def getName(self):
        return self.name

    # Accessor for the names of the neighbors to the current node
    def getNeighbors(self):
        return self.neighbors.keys()

    # Accessor for the weights of the neighbors to the current node
    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

    # Add a neighbor to the current node, with the default being no weight
    def addNeighbor(self, neighbor, weight = 0):
        self.neighbors[neighbor] = weight

# Defines a Graph using an adjacency list.
class Graph:

    # Initialize a graph with an empty list of nodes
    def __init__(self):
        self.nodeList = {}
        self.nodeCount = 0
        self.pre = {}
        self.post = {}
        self.clock = 0

    # Allow iterations over nodes
    def __iter__(self):
        return iter(self.nodeList.values())
    
    # Import a graph from a file. Each line should contain the two nodes that
    # an edge goes between, separated by a tab.
    # ONLY WORKS FOR UNWEIGHTED GRAPHS
    def importFromFile(self, graph):
        fopen = open(graph, "r")
        graphList = fopen.read().splitlines()
        
        for pair in graphList:
            pair = pair.split("\t")
            self.addEdge(pair[0],pair[1])

    # Add a node of a given name, and increment the amount of nodes
    def addNode(self, name):
        self.nodeCount += 1
        self.nodeList[name] = Node(name)

    # Add an edge from source to dest, creating source and dest if they do not 
    # exist
    def addEdge(self, source, dest, weight = 0):
        if source not in self.nodeList:
            self.addNode(source)
        if dest not in self.nodeList:
            self.addNode(dest)
        self.nodeList[source].addNeighbor(self.nodeList[dest], weight)

    # Get all nodes in the current graph
    def getNodes(self):
        return self.nodeList.keys()

    # Depth-First-Search on self
    def DFS(self):
        for node in self:
            node.visited = False

        for node in self:
            if node.visited == False:
                self.explore(node)

    # Explore from a given node, and mark current node as visited
    def explore(self, node):
        node.visited = True
        self.preVisit(node)
        for neighbor in node.getNeighbors():
            if neighbor.visited == False:
                self.explore(neighbor)
        self.postVisit(node)

    def preVisit(self, node):
        self.pre[node] = self.clock
        self.clock += 1

    def postVisit(self, node):
        self.post[node] = self.clock
        self.clock += 1


def main():
    graphFile = sys.argv[1]
    graph = Graph()
    graph.importFromFile(graphFile)
    graph.DFS()

if __name__ == "__main__":
    main()
