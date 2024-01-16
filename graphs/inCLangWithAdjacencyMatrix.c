#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define V 6 // Number of vertices

// Structure to represent a graph with an adjacency matrix
struct Graph {
    int matrix[V][V];
};

// Function to create a graph with an adjacency matrix
struct Graph* createGraph() {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));

    // Initialize the matrix with zeros (no edges initially)
    for (int i = 0; i < V; ++i)
        for (int j = 0; j < V; ++j)
            graph->matrix[i][j] = 0;

    return graph;
}

// Function to add an edge to the graph
void addEdge(struct Graph* graph, int src, int dest) {
    graph->matrix[src][dest] = 1;
    graph->matrix[dest][src] = 1; // For undirected graph
}

// Function to perform Breadth-First Search (BFS)
void BFS(struct Graph* graph, int start) {
    int queue[V];
    int front = 0, rear = 0;
    int visited[V] = {0};

    queue[rear++] = start;
    visited[start] = 1;

    printf("BFS starting from vertex %d: ", start);

    while (front < rear) {
        int current = queue[front++];
        printf("%d ", current);

        for (int i = 0; i < V; ++i) {
            if (graph->matrix[current][i] && !visited[i]) {
                queue[rear++] = i;
                visited[i] = 1;
            }
        }
    }

    printf("\n");
}

// Function to perform Depth-First Search (DFS)
void DFSUtil(struct Graph* graph, int v, int* visited) {
    visited[v] = 1;
    printf("%d ", v);

    for (int i = 0; i < V; ++i) {
        if (graph->matrix[v][i] && !visited[i])
            DFSUtil(graph, i, visited);
    }
}

void DFS(struct Graph* graph, int start) {
    int visited[V] = {0};

    printf("DFS starting from vertex %d: ", start);
    DFSUtil(graph, start, visited);
    printf("\n");
}

// Function to perform Dijkstra's Algorithm
void Dijkstra(struct Graph* graph, int start) {
    int distance[V];
    int visited[V];

    for (int i = 0; i < V; ++i) {
        distance[i] = INT_MAX;
        visited[i] = 0;
    }

    distance[start] = 0;

    printf("Dijkstra's Algorithm starting from vertex %d:\n", start);

    for (int count = 0; count < V - 1; ++count) {
        int minDist = INT_MAX, minIndex;

        for (int v = 0; v < V; ++v) {
            if (!visited[v] && distance[v] < minDist) {
                minDist = distance[v];
                minIndex = v;
            }
        }

        visited[minIndex] = 1;

        for (int i = 0; i < V; ++i) {
            if (!visited[i] && graph->matrix[minIndex][i] && distance[minIndex] != INT_MAX &&
                distance[minIndex] + 1 < distance[i]) {
                distance[i] = distance[minIndex] + 1;
            }
        }
    }

    for (int i = 0; i < V; ++i)
        printf("Shortest distance from vertex %d to %d: %d\n", start, i, distance[i]);
}

// Main function
int main() {
    // Create a graph with an adjacency matrix
    struct Graph* graph = createGraph();

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
    DFS(graph, 0);
    Dijkstra(graph, 0);

    return 0;
}
