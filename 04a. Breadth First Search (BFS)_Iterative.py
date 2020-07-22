from collections import deque


# class to represent a graph object:
class Graph:
    # Constructor
    def __init__(self, edges, N):

        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# Perform BFS on graph starting from vertex v
def BFS(graph, v, discovered):

    # create a queue used to do BFS
    q = deque()

    # mark source vertex as discovered
    discovered[v] = True

    # push source vertex into the queue
    q.append(v)

    # run till queue is not empty
    while q:

        # pop front node from queue and print it
        v = q.popleft()
        print(v, end=' ')

        # do for every edge (v -> u)
        for u in graph.adjList[v]:
            if not discovered[u]:
                # mark it discovered and push it into queue
                discovered[u] = True
                q.append(u)


if __name__ == '__main__':

    # List of graph edges as per above diagram
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
        # vertex 0, 13 and 14 are single nodes
    ]

    # Set number of vertices in the graph
    N = 15

    # create a graph from edges
    graph = Graph(edges, N)

    # stores vertex is discovered or not
    discovered = [False] * N

    # Do BFS traversal from all undiscovered nodes to
    # cover all unconnected components of graph
    for i in range(N):
        if not discovered[i]:
            # start BFS traversal from vertex i
            BFS(graph, i, discovered)
