class Graph:

    def __init__(self, vertices):
        self.V = vertices
        
        # create matrix filled with 0
        self.graph = []
        for i in range(vertices):
            row = []
            for j in range(vertices):
                row.append(0)
            self.graph.append(row)

    # add edge
    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    # prim function
    def prim(self):

        selected = [False] * self.V
        selected[0] = True

        no_edge = 0
        total = 0

        print("Edges in MST")

        while no_edge < self.V - 1:

            minimum = 999
            x = 0
            y = 0

            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if (not selected[j]) and self.graph[i][j] != 0:
                            if minimum > self.graph[i][j]:
                                minimum = self.graph[i][j]
                                x = i
                                y = j

            print(x, "-", y, ":", self.graph[x][y])
            total += self.graph[x][y]
            selected[y] = True
            no_edge += 1

        print("Total cost =", total)


# create graph
g = Graph(8)

g.add_edge(0,1,14)
g.add_edge(0,6,8)
g.add_edge(1,2,15)
g.add_edge(1,3,14)
g.add_edge(1,5,13)
g.add_edge(1,7,26)
g.add_edge(2,3,12)
g.add_edge(3,4,10)
g.add_edge(3,5,12)
g.add_edge(4,5,10)
g.add_edge(4,6,14)
g.add_edge(5,6,21)
g.add_edge(6,7,7)

g.prim()