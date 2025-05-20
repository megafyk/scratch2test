class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # bfs + topo
        # time O(n+e), space O(n+e)
        indegree = [0] * n
        adj = defaultdict(list)
        for u,v in edges:
            indegree[u] += 1
            indegree[v] += 1
            adj[u].append(v)
            adj[v].append(u)
        q = deque()
        visit = [False] * n 
        res = []
        for i in range(n):
            if indegree[i] == 1 or indegree[i] == 0:
                q.append(i)
                visit[i] = True
                res.append(i)
        
        while q:
            res = []
            for _ in range(len(q)):
                u = q.popleft()
                res.append(u)
                indegree[u] -= 1
                for v in adj[u]:
                    if not visit[v]:
                        indegree[v] -= 1
                        if indegree[v] == 1:
                            q.append(v)
                            visit[v] = True

        return res      

        