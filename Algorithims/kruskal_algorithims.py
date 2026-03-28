class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def kruskal(self):

        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        for node in range(self.V):
            parent.append(node)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, x, y)

        print("Edges in MST")

        total = 0
        for u, v, w in result:
            print(u, "-", v, ":", w)
            total += w

        print("Total cost =", total)


g = Graph(6)

g.add_edge(0,1,10)
g.add_edge(0,3,30)
g.add_edge(1,5,25)
g.add_edge(2,5,15)
g.add_edge(3,5,20)
g.add_edge(2,4,35)
g.add_edge(1,4,40)
g.add_edge(0,4,45)
g.add_edge(1,2,50)
g.add_edge(4,5,55)

g.kruskal()