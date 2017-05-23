from Graph import *

g = Graph()
for i in range(6):
    g.addVertex(i)


g.vertexesList
g.getVertices()


g.addEdge(0,1,2)
g.addEdge(1,2,5)
g.addEdge(1,3,4)

print(g.vertexesList)
print(g.getVertices())

vert = g.getVertex(1)
print(vert.getConnections())
