import disjointSet as dst

class Graph:
  def __init__(self,vertices) -> None:
    self.V = vertices
    self.graph = []
    self.nodes = []
    self.MST = []

  def addEdge(self,s,d,w): # source,destination,weight
    self.graph.append([s,d,w])
  
  def addNode(self,value):
    self.nodes.append(value)

  def print_solution(self,s,d,w):
    for s,d,w in self.MST:
      print("%s - %s: %s" % (s,d,w))

  def kruskal_algorithm(self):
    i,e = 0,0 # i for index, e for edge
    ds = dst.DisjointSet(self.nodes)
    self.graph = sorted(self.graph,key=lambda item:item[2]) # sorting the graph
    while e < self.V - 1: # Loop until we have included (V-1) edges in the MST
      s,d,w = self.graph[i] # Get the current edge (source, destination, weight)
      i += 1
      # Find the set identifiers for the source and destination nodes
      x = ds.find(s)
      y = ds.find(d)
      if x != y:  # If the source and destination nodes are not in the same set (avoiding cycles)
        self.MST.append([s,d,w]) # add edge to MST
        ds.union(x,y) # merge the two sets
        e += 1
      
    self.print_solution(s,d,w)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskal_algorithm()
