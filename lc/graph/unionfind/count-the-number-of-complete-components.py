class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def check_complete(start):
            q = deque()
            q.append(start)
            cnt_v = cnt_e = 0
            visit.add(start)
            while q:
                u = q.popleft()
                cnt_v += 1
                cnt_e += len(adj[u])
                for v in adj[u]:
                    if v not in visit:
                        visit.add(v)
                        q.append(v)
            return cnt_e == (cnt_v - 1) * (cnt_v)

        res = 0
        for u in range(n):
            if u in visit:
                continue
            if check_complete(u):
                res += 1
        return res


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, u):
        if u != self.par[u]:
            self.par[u] = self.find(self.par[u])  # Path compression
        return self.par[u]

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return

        if p1 < p2:
            self.par[p2] = p1
        else:
            self.par[p1] = p2


class Solution1:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # graph union find
        # time O(E + VlogV + V^2), space O(V)
        uf = UnionFind(n)
        graph = defaultdict(list)

        for u, v in edges:
            uf.union(u, v)
            graph[u].append(v)
            graph[v].append(u)

        components = defaultdict(list)
        for i in range(n):
            p = uf.find(i)
            components[p].append(i)

        res = 0

        for r, arr in components.items():
            completed = True
            for u in arr:
                if len(graph[u]) + 1 != len(arr):
                    completed = False
                    break
            res += 1 if completed else 0
        return res
