import sys

class Graph:

    def __init__(self, vertecies = None, edges = None):
        self.vertecies = vertecies if vertecies is not None else []
        self.edges = []

    def importFromFile(self, file):

        fopen = open(file, "r")
        graphList = fopen.read().splitlines()

        for pair in graphList:
            print pair
            pair = pair.split("\t")
            self.vertecies.append(pair[0])
            self.edges.append(pair[1])

            print self.vertecies
            print self.edges

        return graphList

def main():
    file = sys.argv[1]
    graph = Graph()
    graph.importFromFile(file)

if __name__ == "__main__":
    main()
