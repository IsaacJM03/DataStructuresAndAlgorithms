class DisjointSet:
  def __init__(self,vertices) -> None:
    self.vertices = vertices
    self.parent = {}
    for v in vertices:
      self.parent[v] = v
    self.rank = dict.fromkeys(vertices,0) # creating new dictionary

  def find(self,item):
    if self.parent[item] == item:
      return item
    else:
      return self.find(self.parent[item])
    
  def union(self,x,y):
    xroot = self.find(x)
    yroot = self.find(y)
    # setting parents of these sets
    if self.rank[xroot] < self.rank[yroot]:
      self.parent[xroot] = yroot
    elif self.rank[xroot] > self.rank[yroot]:
      self.parent[yroot] = xroot
    else:
      self.parent[yroot] = xroot
      self.rank[xroot] += 1


# vertices = ["A","B","C","D","E","F","G"]
# ds = DisjointSet(vertices)
# ds.union("A","B")
# ds.union("A","G")
# print(ds.find("G"))