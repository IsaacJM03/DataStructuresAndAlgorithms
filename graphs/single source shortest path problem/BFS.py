class Graph:
  def __init__(self,gdict=None) -> None:
    if gdict is None:
      gdit = {}
    self.gdict = gdict

  def BFS(self,start,end):
    queue = []
    queue.append([start]) # add first element to queue
    while queue: # is not empty
      path = queue.pop(0)
      node = path[-1] # get last element
      if node == end:
        return path
      for adjacent in self.gdict.get(node,[]): # get all adjacent nodes to current one
        newPath = list(path) # copy path
        newPath.append(adjacent) # add adjacent
        queue.append(newPath) # add new path to queue

customDict = {
  "a": ["b","c"],
  "b": ["d"],
  "c": ["d","e"],
  "d": ["f"],
  "e": ["f"],
  "g": ["f"]  
}

customGraph = Graph(customDict)
print(customGraph.BFS("a","d"))