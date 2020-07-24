from collections import deque


# class to represent a graph object:
class Graph:

    # stores indegree of a vertex
    indegree = None

    # Constructor
    def __init__(self, edges, N):

        # A List of Lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]

        # initialize indegree of each vertex by 0
        self.indegree = [0] * N

        # add edges to the undirected graph
        for (src, dest) in edges:

            # add an edge from source to destination
            self.adjList[src].append(dest)

            # increment in-degree of destination vertex by 1
            self.indegree[dest] = self.indegree[dest] + 1


# performs Topological Sort on a given DAG
def doTopologicalSort(graph, N):

    # list to store the sorted elements
    L = []

    # get in-degree information of the graph
    indegree = graph.indegree

    # Set of all nodes with no incoming edges
    S = deque([i for i in range(N) if indegree[i] == 0])

    while S:

        # remove a node n from S
        n = S.pop()

        # add n to tail of L
        L.append(n)

        for m in graph.adjList[n]:

            # remove edge from n to m from the graph
            indegree[m] = indegree[m] - 1

            # if m has no other incoming edges then
            # insert m into S
            if indegree[m] == 0:
                S.append(m)

    # if graph has edges then graph has at least one cycle
    for i in range(N):
        if indegree[i]:
            return None

    return L


if __name__ == '__main__':

    # List of graph edges as per above diagram
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]

    # Set number of vertices in the graph
    N = 8

    # create a graph from edges
    graph = Graph(edges, N)

    # Perform Topological Sort
    L = doTopologicalSort(graph, N)

    if L:
        print(L)  # print topological order
    else:
        print("Graph has at least one cycle. Topological sorting is not possible.")
