#include<stdio.h>
#include<stdlib.h>

// representing a node in the adjacency list
struct Node
{
  int dest;//destination
  struct Node *next;//pointer to the next node
};

// representing the adjacency list
struct AdjList
{
  struct Node *head;
};

// structure to represent a graph with an array of adjacency lists
struct Graph
{
  int V; // number of vertices
  struct AdjList* array;
};

struct Graph *createGraph(int V)
{
  struct Graph *graph = (struct Graph*)malloc(sizeof(struct Graph));
  graph->V = V;

  // create an array of adjacency lists
  graph->array = (struct AdjList*)malloc(V * sizeof(struct AdjList));

  // initialize each adajcency list as empty
  for (int i = 0; i < V; ++i)
  {
    graph->array[i].head = NULL;
  }
  return graph;
};

void addEdge(struct Graph *graph,int src,int dest)
{
  // add an edge(node) from src(source) to dest
  struct Node *node = (struct Node*)malloc(sizeof(struct Node));
  node->dest = dest;
  node->next = graph->array[src].head;
  graph->array[src].head = node;

  // for an undirected graph, add an edge(node) from dest to src(source)
  node = (struct Node*)malloc(sizeof(struct Node));
  node->dest = src;
  node->next = graph->array[dest].head;
  graph->array[dest].head = node;
}

void BFS(struct Graph *graph, int start)
{
  // create a queue
  int *queue = (int*)malloc(sizeof(int)*graph->V);
  int front = 0;
  int rear = 0;

  // array to keep track of visited vertices
  int *visited = (int*)malloc(sizeof(int)*graph->V);
  for (int i = 0;i < (graph->V);++i)
  {
    visited[i] = 0;
  }

  // enqueue the start vertex and mark it as visited
  queue[rear++] = start;
  visited[start] = 1;

  printf("BFS starting from vertex %d:",start);

  while (front < rear) // why? because we need to keep checking the queue until it is empty
  {
    int current = queue[front++];
    printf("%d",current);

    // explore adjacent vertices
    struct Node *temp = graph->array[current].head;
    while (temp!=NULL) // keep adding values to the queue
    {
      int neighbour = temp->dest;
      if (!visited[neighbour])
      {
        queue[rear++] = neighbour;  // enqueue the neighbour
        visited[neighbour] = 1;
      }
      temp = temp->next;
      
    }
    
  }

  printf("\n");

  free(queue);
  free(visited);
  
}

void DFSUtil(struct Graph *graph, int v, int *visited)
{
  visited[v] = 1;
  printf("%d",v);

  struct Node *temp = graph->array[v].head;
  while (temp!=NULL)
  {
    int neighbour = temp->dest;
    if (!visited[neighbour])
    {
      DFSUtil(graph,neighbour,visited); // recursive call to visit all adjacent vertices
    }
    temp = temp->next;
  }
  
}

void DFS(struct Graph *graph,int start)
{
  int *visited = (int*)malloc(graph->V * sizeof(int));
  for (int i=0;i < graph->V;++i) // keep increasing the value before as well using ++i instead of i++
  {
    visited[i] = 0;

    printf("DFS starting from vertex %d:",start);
    DFSUtil(graph,start,visited);
    printf("\n");

  }
  free(visited);

}

void Dijkstra(struct Graph *graph,int start)
{
  // array to store the distance from the start vertex to each vertex
  int *distance = (int*)malloc(graph->V * sizeof(int));
  for (int i=0;i < graph->V;++i)
  {
    distance[i] = __INT_MAX__;
  }

  // Array to keep track of visited vertices
  int *visited = (int*)malloc(graph->V * sizeof(int));
  for (int i=0;i < graph->V;++i)
  {
    visited[i] = 0;
  }

  // distance from the start vertex to itself is 0
  distance[start] = 0;

  printf("Dijkstra's Algorithm starting from vertex %d:\n",start);

  for (int count = 0; count < graph->V; ++count)
  {
    // Find the vertex with the minimum distance value from the set of vertices not yet included
    int minDist = __INT_MAX__,minIndex;
    for(int v=0;v < graph->V;++v)
    {
      if (!visited[v] && distance[v] < minDist)
      {
        minDist = distance[v];
        minIndex = v;
      }
    }
    
    // Mark the minimum distance vertex as visited
    visited[minIndex] = 1;

    // update distance values of adjacent vertices
    struct Node *temp = graph->array[minIndex].head;
    while (temp!=NULL)
    {
      int neighbour = temp->dest;
      if(!visited[neighbour] && distance[minIndex] != __INT_MAX__ && distance[minIndex]+1 < distance[neighbour]) // if the distance is not infinity and the distance is less than the current distance and the neighbour is not visited
      {
        distance[neighbour] = distance[minIndex] + 1; // update the distance
      }
      temp = temp->next;
    }
    
  }

  // Print the shortesst distances
  for(int i=0;i < graph->V;++i)
  {
    printf("Shortest distance from %d to %d is %d \n",start,i,distance[i]);
  }
  printf("\n");
  
  free(distance);
  free(visited);
  
}


int main() {
    // Create a graph with 6 vertices
    struct Graph* graph = createGraph(6);

    // Add edges to the graph
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 2, 4);
    addEdge(graph, 3, 5);
    addEdge(graph, 4, 5);

    // Perform BFS, DFS, and Dijkstra's Algorithm
    BFS(graph, 0);
    DFS(graph, 1);
    Dijkstra(graph, 0);

    return 0;
}
