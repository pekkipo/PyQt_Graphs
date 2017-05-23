from Vertex import *


class Graph:
    def __init__(self):
        self.vertexesList = {}  # modeling as adjacency list
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertexesList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertexesList:
            return self.vertexesList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertexesList

    def addEdge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vertexesList:
            nv = self.addVertex(from_vertex)
        if to_vertex not in self.vertexesList:
            nv = self.addVertex(to_vertex)
        self.vertexesList[from_vertex].addNeighbor(self.vertexesList[to_vertex], cost)

    def getVertices(self):
        return self.vertexesList.keys()

    def getVertices_values(self):
        return self.vertexesList.values()

    def getVertices_items(self):
        return self.vertexesList.items()

    def __iter__(self):
        return iter(self.vertexesList.values())