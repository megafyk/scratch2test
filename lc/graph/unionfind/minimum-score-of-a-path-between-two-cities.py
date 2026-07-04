class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]

    def find(self, u):
        if self.par[u] != u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)
        if p1 == p2:
            return

        if p1 < p2:
            self.par[p2] = p1
        elif p1 > p2:
            self.par[p1] = p2


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # unionfind
        # time O(n), space O(n)
        uf = UnionFind(n)
        score = [inf for i in range(n + 1)]
        for u, v, w in roads:
            uf.union(u, v)
            p = uf.find(u)
            mi = min(score[u], score[v], score[p], w)
            score[u] = score[v] = score[p] = mi

        res = inf
        for u in range(1, n + 1):
            if uf.find(u) == 1:
                res = min(res, score[u])
        return res


class Solution1:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # bfs
        # time O(n), space O(n)
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        q = deque()
        q.append(1)
        visit = set()
        visit.add(0)
        res = inf
        while q:
            u = q.popleft()
            for v, w in adj[u]:
                res = min(res, w)
                if v not in visit:
                    q.append(v)
                    visit.add(v)
        return res
