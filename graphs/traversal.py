class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
  
    def BFS(self,vertex):
      visited = [vertex]
      queue = [vertex]
      while queue: # is not empty or has elements
        deVertex = queue.pop(0) #always take the first
        print(deVertex)
        for adjacentVertex in self.gdict[deVertex]: # looping through the graph to check adjacent vertices to current vertex
           if adjacentVertex not in visited:
              visited.append(adjacentVertex)
              queue.append(adjacentVertex)
    

    def DFS(self,vertex):
       visited = [vertex]
       stack = [vertex]
       while stack:
          popVertex = stack.pop() # take the top on the stack
          print(popVertex)
          for adjacentVertex in self.gdict[popVertex]:
             if adjacentVertex not in visited:
                visited.append(adjacentVertex)
                stack.append(adjacentVertex)


customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }

testGraph = Graph(customDict)
testGraph.BFS("b")
print('-----------------')
testGraph.DFS("b")