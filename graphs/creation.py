# class Graph:
#   def __init__(self,gdict=None):
#     if gdict is None:
#       gdict = {}
#     self.gdict = gdict

#   def addEdge(self,vertex,edge):
#     self.gdict[vertex].append(edge)

# customDict = {
#   'a':['b','c'],
#   'b':['a','d'],
#   'c':['a','e'],
# }


class Graph:
  def __init__(self):
    self.adjacency_list = {}

  def add_vertex(self,vertex):
    if vertex not in self.adjacency_list.keys():
      self.adjacency_list[vertex] = []
      return True
    return False
  
  def print_graph(self):
    for vertex in self.adjacency_list:
      print(vertex,":",self.adjacency_list[vertex])
  
  def add_edge(self,vertex1,vertex2):
    if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
      self.adjacency_list[vertex1].append(vertex2)
      self.adjacency_list[vertex2].append(vertex1)
      return True
    return False

  def remove_edge(self,vertex1,vertex2):
    if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
      try:
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
      except:
        pass
      return True
    return False

  def remove_vertex(self,vertex):
    if vertex in self.adjacency_list.keys():
      for other_vertex in self.adjacency_list[vertex]:
        self.adjacency_list[other_vertex].remove(vertex)
      del self.adjacency_list[vertex]
      return True
    return False

testGraph = Graph()
testGraph.add_vertex("A")
testGraph.add_vertex("B")
testGraph.add_vertex("C")
testGraph.add_vertex("D")
testGraph.add_edge("A","B")
testGraph.add_edge("A","C")
testGraph.add_edge("A","D")
testGraph.add_edge("B","C")
testGraph.add_edge("C","D")
testGraph.print_graph()
print('After Removal...')
testGraph.remove_edge("A","B")
testGraph.remove_vertex("C")
testGraph.print_graph()