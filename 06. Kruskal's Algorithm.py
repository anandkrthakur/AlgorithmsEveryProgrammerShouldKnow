# class to represent a disjoint set:
class DisjointSet:
    parent = {}

    # perform MakeSet operation
    def makeSet(self, N):

        # create N disjoint sets (one for each vertex)
        for i in range(N):
            self.parent[i] = i

    # Find the root of the set in which element k belongs
    def Find(self, k):

        # if k is root
        if self.parent[k] == k:
            return k

        # recur for parent until we find root
        return self.Find(self.parent[k])

    # Perform Union of two subsets
    def Union(self, a, b):

        # find root of the sets in which elements
        # x and y belongs
        x = self.Find(a)
        y = self.Find(b)

        self.parent[x] = y


# construct MST using Kruskal's algorithm
def KruskalAlgo(edges, N):
    # stores edges present in MST
    MST = []

    # initialize DisjointSet class # create singleton set for each element of universe:
    ds = DisjointSet()
    ds.makeSet(N)

    index = 0

    # MST contains exactly V-1 edges
    while len(MST) != N - 1:

        # consider next edge with minimum weight from the graph
        (src, dest, weight) = edges[index]
        index = index + 1

        # find root of the sets to which two endpoint
        # vertices of next_edge belongs
        x = ds.Find(src)
        y = ds.Find(dest)

        # if both endpoints have different parents, they beto
        # different connected components and can be included in MST
        if x != y:
            MST.append((src, dest, weight))
            ds.Union(x, y)

    return MST


if __name__ == '__main__':

    # (u, v, w) Triplet represent undirected edge from
    # vertex u to vertex v having weight w
    edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9), (1, 4, 7), (2, 4, 5),
        (3, 4, 15), (3, 5, 6), (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]

    # sort edges by increasing weight
    edges.sort(key=lambda x: x[2])

    # Number of vertices in the graph
    N = 7

    # construct graph
    e = KruskalAlgo(edges, N)

    print(e)
