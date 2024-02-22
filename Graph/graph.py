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
        
        print(self.adjacentList)
        
        return self
                



my_graph = Graph()
my_graph.addVertex("start")
my_graph.addVertex("second")
my_graph.addVertex("friedn")
my_graph.addVertex("start").addEdge('start','second').addEdge('second','friedn')
