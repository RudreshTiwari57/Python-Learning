class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        if v in self.graph:
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    self.dfs_util(neighbour, visited)

    def dfs(self, start):
        visited = set()
        print("DFS Traversal starting from node", start, ":")
        self.dfs_util(start, visited)
        print()



g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.dfs(2)
