class Edge:
  def __init__(self,weight,start_vertex,target_vertex) -> None:
    self.weight = weight
    self.start_vertex = start_vertex
    self.target_vertex = target_vertex

class Node:
  def __init__(self,name) -> None:
    self.name = name
    self.visited = False
    self.predecessor = None # previous node
    self.neighbors = []
    self.min_distance = float("inf")

  def __lt__(self,other_node):
    return self.min_distance < other_node.min_distance #  for priority queue, min heap,

  def add_edge(self,weight,destination_vertex):
    edge = Edge(weight,self,destination_vertex)
    self.neighbors = []
    

class Dijkstra:
  def __init__(self):
    self.heap = []

  def calculate( 
