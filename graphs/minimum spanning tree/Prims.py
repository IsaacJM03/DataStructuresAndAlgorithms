import sys

class Graph:
  def __init__(self,vertexNum,edges,nodes) -> None:
    self.edges = edges # list of edges
    self.nodes = nodes # node names
    self.vertexNum = vertexNum # total number of vertices
    self.MST = [] # empty list to store edges of the minimum spanning tree

  def print_solution(self):
    print("Edge : Weight")
    for s,d,w in self.MST:
      print("%s -> %s : %s" % (s,d,w))

  def prims_algorithm(self):
    visited = [0]*self.vertexNum # list to keep track of visited nodes
    edgeNum = 0 # initialize edge counter
    visited[0] = True # set the first node as visited

    # Loop until we have included (V-1) edges in the MST
    while edgeNum < self.vertexNum - 1:
      min = sys.maxsize # track the min value
      # Iterate through all visited nodes
      for i in range(self.vertexNum):
        if visited[i]:
        # Iterate through all neighboring nodes of the current visited node
          for j in range(self.vertexNum):
            # If the neighboring node is not visited and there's an edge between them
            if(not visited[j]) and self.edges[i][j]:
              # If the weight of this edge is less than the current minimum
              if self.edges[i][j] < min:
                
                min = self.edges[i][j] # Update the minimum edge weight and store the source and destination nodes
                s = i
                d = j

      self.MST.append([self.nodes[s],self.nodes[d],min]) # add minimum edge to MST
      visited[d] = True
      edgeNum += 1

    self.print_solution()


# Create an adjacency matrix to represent the graph's edges
edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]
nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.prims_algorithm()
