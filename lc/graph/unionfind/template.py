class Solution:
    def __init__(self, n) -> None:
        self.par = list(range(n))

    def find(self, cur):
        if cur != self.par[cur]:
            cur = self.find(self.par[cur])
        return self.par[cur]

    def union(self, u, v):
        # n is number of vertices
        # node -> node edges = [[1,2],[2,3],[3,1]]
        # init parrent root
        # find step
        p1 = self.find(u)
        p2 = self.find(v)

        # i,j has same root <=> i,j same set
        if p1 == p2:
            return

        # union step
        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
