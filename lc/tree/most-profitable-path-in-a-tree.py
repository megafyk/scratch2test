class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # tree traversal
        # time O(N), space O(N)
        n = len(amount)
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        b_path = {}
        b_path[bob] = 0
        # bob traversal's turn
        def dfs(node, par, time):
            if node == 0: return True
            for nei in adj[node]:
                if nei == par: continue
                if dfs(nei,node,time + 1):
                    b_path[nei] = time + 1                    
                    return True
            return False

        # find bob only path
        dfs(bob, -1, 0)

        # alice traversal's turn
        q = deque([(0, 0, -1, amount[0])])
        res = -sys.maxsize
        while q:
            node, time, par, profit = q.popleft()
            for nei in adj[node]:
                if nei == par: continue
                nei_profit = amount[nei]
                nei_time = time + 1
                if nei in b_path:
                    if nei_time == b_path[nei]:
                        nei_profit = amount[nei] // 2
                    if nei_time > b_path[nei]:
                        nei_profit = 0

                q.append((nei, time + 1, node, profit + nei_profit))
                if len(adj[nei]) == 1:
                    res = max(res, profit + nei_profit)
        return res