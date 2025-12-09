class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # graph dfs with hashmap
        # time O(n*(n+E) + q), space O(n^2)
        hm = defaultdict(set) # v is preq u => hm[u] = {v}  
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)

        visit = [False] * numCourses
        def dfs(node):
            if visit[node]:
                return hm[node]
            visit[node] = True
            for nei in adj[node]:
                hm[node].add(nei)
                pres = dfs(nei)
                for pre in pres:
                    hm[node].add(pre)
            return hm[node]
            
        for n in range(numCourses):
            dfs(n)
        
        res = [False] * len(queries)
        for idx,(u,v) in enumerate(queries):
            if u in hm[v]:
                res[idx] = True
        return res
    
class Solution1:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # floyd-warshall
        # time O(n^3), space O(n^2)
        dp = [[False] * numCourses for _ in range(numCourses)]

        for i, j in prerequisites:
            dp[i][j] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])
        res = []
        for u, v in queries:
            res.append(dp[u][v])
        return res

class Solution2:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # tle
        indegree = [set() for _ in range(numCourses)]
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v].add(u)
        
        q = deque()

        for u in range(numCourses):
            if not indegree[u]:
                q.append(u)
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                for p in indegree[u]:
                    indegree[v].add(p) # tle because of this overhead op
                q.append(v)
                

        res = []
        for u,v in queries:
            check = False
            if u in indegree[v]:
                check = True
            res.append(check)
        return res