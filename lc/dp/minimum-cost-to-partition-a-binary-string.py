class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        # dfs
        # n = len(s)
        # time O(n), space O(n)
        n = len(s)
        prefix = [0] * n
        prefix[0] = 1 if s[0] == "1" else 0
        for i in range(1, n):
            prefix[i] = (1 if s[i] == "1" else 0) + prefix[i-1]
        
        def cost(i, j):
            X = prefix[j] - (prefix[i-1] if i > 0 else 0)
            if X == 0:
                return flatCost
            return (j-i+1) * X * encCost

        def dfs(i,j):
            if (j-i+1) % 2:
                return cost(i, j)
            mid = i + (j-i) // 2
            
            return min(cost(i, j), dfs(i, mid) + dfs(mid+1, j))

        return dfs(0,n-1)