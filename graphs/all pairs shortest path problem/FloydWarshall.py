INF = float("inf")

def print_solution(nV,distance): # where nV is number of vertices
  for i in range(nV):
    for j in range(nV):
      if(distance[i][j] == INF):
        print("INF",end=" ")
      else:
        print(distance[i][j], end=" ")
    print(" ")

def floyd_warshall(nV,G):
  distance = G
  for k in range(nV):
    for i in range(nV):
      for j in range(nV):
        distance[i][j] = min(distance[i][j],distance[i][k] + distance[k][j])
  print_solution(nV,distance)


G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]

floyd_warshall(4, G)