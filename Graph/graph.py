from collections import deque

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
        
        # print(self.adjacentList)
        if vertex:
            for edge in vertex:
                self.adjacentList[edge] = [e for e in self.adjacentList[edge] if e != v]
            del self.adjacentList[v]
        # print(self.adjacentList)
        
        return vertex

     
    
    def dfsRecursive(self,vertex):
        res = []
        visited = set()
        
        def dfs(vertex):
            if not vertex:
                return None
            
            visited.add(vertex)
            res.append(vertex)
            
            for con in self.adjacentList[vertex]:
                if not con in visited:
                    dfs(con)
        
        dfs(vertex)
        return res
    
    def dfsIterative(self,start):
        res = []
        s = []
        visited = set()
        
        s.append(start)
        cur_vertex = None
        while s:
            cur_vertex = s.pop()
            
            if not cur_vertex in visited:
                res.append(cur_vertex)
                visited.add(cur_vertex)
                
                for neighbour in self.adjacentList[cur_vertex]:
                    s.append(neighbour)
        return res
    
    def bfs(self,start):
        queue = deque([start])
        res = []
        visited = set()
        current_vertex = None
        
        visited.add(start)
        
        while queue:
            current_vertex = queue.popleft()
            res.append(current_vertex)
            
            for neighbor in self.adjacentList[current_vertex]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
            
        return res
            
        



# my_graph = Graph()
# my_graph.addVertex("start")
# my_graph.addVertex("second")
# my_graph.addVertex("friedn")
# my_graph.addVertex("start").addEdge('start','second').addEdge('second','friedn')
# # my_graph.removeEdge('second','friedn')
# my_graph.removeVertex('start')

# my_graph.showConnections()

g = Graph()

g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")


g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B","D")
g.addEdge("C","E")
g.addEdge("D","E")
g.addEdge("D","F")
g.addEdge("E","F")

# g.showConnections()

dpf = g.dfsRecursive("A")

ite = g.dfsIterative('A')

bfs = g.bfs('A')

print(dpf)
print(ite)
print(bfs)
