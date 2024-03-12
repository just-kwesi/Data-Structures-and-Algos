from collections import deque

# * edge = { node:vertex, weight:int }

class WeightedGraph:
    def __init__(self) -> None:
        self.number_of_vertices = 0
        self.adjacentList = {}
    
    def addVertex(self,value):
        if not self.adjacentList.get(value,None):
            self.adjacentList[value] = []
            self.number_of_vertices += 1
        
        return self
    
    def addEdge(self,vertex1,vertext2,weight):
        if self.adjacentList.get(vertex1,None) != None and \
            self.adjacentList.get(vertext2,None) != None:
            self.adjacentList[vertex1].append({"node": vertext2, "weight": weight})
            self.adjacentList[vertext2].append({"node": vertex1, "weight": weight})
        
        # print(self.adjacentList)
        
        return self
    
    def showConnections(self):
        for key in self.adjacentList:
            # connections = ', '.join(self.adjacentList[key])
            print(f"{key} --> {self.adjacentList[key]}")


g = WeightedGraph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")


g.addEdge("A", "B", 5)
g.addEdge("A", "C", 8)
g.addEdge("B","D", 4)
g.addEdge("C","E", 14)
g.addEdge("D","E" , 8)
g.addEdge("D","F", 1)
g.addEdge("E","F",54)

g.showConnections()