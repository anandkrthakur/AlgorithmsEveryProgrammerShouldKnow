# Recursive Function to print path of given vertex from source vertex
def printPath(parent, vertex):
    if vertex < 0:
        return

    printPath(parent, parent[vertex])
    print(vertex, end=' ')


# Function to run Bellman Ford Algorithm from given source
def bellmanFord(edges, source, N):

    # distance[] and parent[] stores shortest-path (least cost/path) info
    distance = [float('inf')] * N
    parent = [-1] * N

    # Initially all vertices except source vertex have a weight of
    # infinity and a no parent
    distance[source] = 0

    # Relaxation step (run V -1 times)
    for k in range(N - 1):

        # edge from u to v having weight w
        for (u, v, w) in edges:

            # if the distance to the destination v can be
            # shortened by taking the edge u-> v
            if distance[u] + w < distance[v]:

                # update distance to the new lower value
                distance[v] = distance[u] + w

                # set v's parent as u
                parent[v] = u

    # run relaxation step once more for N'th time to
    # check for negative-weight cycles
    for (u, v, w) in edges:  # edge from u to v having weight w

        # if the distance to the destination u can be
        # shortened by taking the edge u-> v
        if distance[u] + w < distance[v]:
            print("Negative Weight Cycle Found!!")
            return

    for i in range(N):
        print("Distance of vertex", i, "from the source is", distance[i], end='.')
        print(" It's path is [ ", end='')
        printPath(parent, i)
        print("]")


if __name__ == '__main__':

    #  of graph edges as per above diagram
    edges = [
        # (x, y, w) -> edge from x to y having weight w
        (0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2),
        (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)
    ]

    # Number of vertices in the graph
    N = 5

    # let source be vertex 0
    source = 0

    # run Bellman Ford Algorithm from given source
    bellmanFord(edges, source, N)
