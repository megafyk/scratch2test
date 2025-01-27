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
        