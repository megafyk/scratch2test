class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        n = len(edges) + 1
        depth = [0] * (n+1)
        
        q = deque([(1,0,0)])
        while q:
            for _ in range(len(q)):
                u,par,dep = q.popleft()
                for v in adj[u]:
                    if v != par:
                        depth[v] = dep + 1
                        q.append((v,u,depth[v]))
        mx_depth = max(depth)
        mod = 10 ** 9 + 7
        return 2**(mx_depth-1) % mod