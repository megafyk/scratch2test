class Solution:
            
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        # dp + graph + dfs
        # time O(n*k*t), space O(n*k*t)
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        
        @cache
        def dfs(u, path, cur_w):
            if cur_w >= t:
                return -1
            if path == k:
                return cur_w
            mx_w = -1
            for v, w in adj[u]:
                mx_w = max(mx_w, dfs(v, path + 1, cur_w + w))
            return mx_w
            
        mx = -1
        for u in range(n):
            mx = max(mx, dfs(u, 0, 0))
        if k == 0: return 0
        return mx