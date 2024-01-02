class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self,startNode,endNode):
      visited = [startNode]
      queue = [startNode]
      path = False
      while queue: # is not empty or has elements
        deVertex = queue.pop(0) #always take the first
        for adjacentVertex in self.gdict[deVertex]: # looping through the graph to check adjacent vertices to current vertex
           if adjacentVertex not in visited:
              if adjacentVertex == endNode:
                path = True
                break
              else:
                visited.append(adjacentVertex)
                queue.append(adjacentVertex)

      return path
    


customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }



g = Graph(customDict)
print(g.checkRoute("a", "i"))