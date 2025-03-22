class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n  # Rank for optimization

    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])  # Path compression
        return self.par[u]

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return

        # Union by rank
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1