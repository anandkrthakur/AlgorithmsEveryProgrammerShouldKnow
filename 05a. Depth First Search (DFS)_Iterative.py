# Class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)


# Function to perform DFS Traversal
def DFS(graph, v, discovered):
    discovered[v] = True  # mark current node as discovered
    print(v, end=' ')  # print current node

    # do for every edge (v -> u)
    for u in graph.adjList[v]:
        if not discovered[u]:  # u is not discovered
            DFS(graph, u, discovered)


# Recursive Python implementation of Depth first search
if __name__ == '__main__':

    # List of graph edges as per above diagram
    edges = [
        # Notice that node 0 is unconnected node
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]

    # Set number of vertices in the graph (0-12)
    N = 13

    # create a graph from edges
    graph = Graph(edges, N)

    # stores vertex is discovered or not
    discovered = [False] * N

    # Do DFS traversal from all undiscovered nodes to
    # cover all unconnected components of graph
    for i in range(N):
        if not discovered[i]:
            DFS(graph, i, discovered)
