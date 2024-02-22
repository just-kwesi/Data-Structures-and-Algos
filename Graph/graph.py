class Graph:
    def __init__(self) -> None:
        self.number_of_vertices = 0
        self.adjacentList = {}
    
    def addVertex(self,value):
        if not self.adjacentList.get(value,None):
            self.adjacentList[value] = []
            self.number_of_vertices += 1
        
        return self
    
    def addEdge(self,value1,value2):
        if self.adjacentList.get(value1,None) != None and \
            self.adjacentList.get(value2,None) != None:
            self.adjacentList[value1].append(value2)
            self.adjacentList[value2].append(value1)
        
        # print(self.adjacentList)
        
        return self
    
    def removeEdge(self,v1,v2):
        # print(self.adjacentList)
        if self.adjacentList.get(v1,None) != None and \
            self.adjacentList.get(v2,None) != None:
            self.adjacentList[v1] = [e for e in self.adjacentList[v1] if e != v2]
            self.adjacentList[v2] = [e for e in self.adjacentList[v2] if e != v1]
        
        # print(self.adjacentList)
        return self
    
    def removeVertex(self,v):
        vertex = self.adjacentList.get(v,None)
        
        print(self.adjacentList)
        if vertex:
            for edge in vertex:
                self.adjacentList[edge] = [e for e in self.adjacentList[edge] if e != v]
            del self.adjacentList[v]
        print(self.adjacentList)
        
        return vertex



my_graph = Graph()
my_graph.addVertex("start")
my_graph.addVertex("second")
my_graph.addVertex("friedn")
my_graph.addVertex("start").addEdge('start','second').addEdge('second','friedn')
# my_graph.removeEdge('second','friedn')
my_graph.removeVertex('start')