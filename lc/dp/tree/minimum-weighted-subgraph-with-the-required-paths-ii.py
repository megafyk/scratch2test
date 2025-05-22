from math import log2
from collections import defaultdict


class Solution:
    def minimumWeight(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        # tree + dp binary lifting
        # time O(nlogn + qlogn), space O(n)
        n = len(edges) + 1 # Number of nodes
        
        # Determine the maximum log level for binary lifting
        # Max height can be n-1. log2(n-1) gives us the max power.
        # If n=1, (0).bit_length() is 0. If n=2, (1).bit_length() is 1.
        # This will be used as the column size for dp table (0 to MAX_LOG-1)
        # And as the upper bound for j in lca loop
        MAX_LOG = (n - 1).bit_length() if n > 1 else 1 # Ensure at least 1 for n=1
        
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        dist = [0] * n  # dist[i] = distance from 0 to i
        height = [0] * n  # height of a node from 0
        # dp[u][j] -> 2^j-th ancestor of node u
        dp = [[0] * MAX_LOG for _ in range(n)] 

        def dfs(u, p):
            # Set parent for binary lifting table
            dp[u][0] = p 
            
            # Precompute 2^j-th ancestors
            for j in range(1, MAX_LOG):
                dp[u][j] = dp[dp[u][j - 1]][j - 1]

            for v, w in adj[u]:
                if v == p: # Don't go back to parent
                    continue
                dist[v] = dist[u] + w
                height[v] = height[u] + 1
                dfs(v, u) # Recurse for child

        # This helper function is correct for floor(log2(n))
        # But its usage in LCA needs to be careful
        def get_log2_floor(num):
            if num <= 0: # For height, it should always be >= 0
                return -1 
            return num.bit_length() - 1

        def lca(u: int, v: int) -> int:
            # Step 1: Bring both nodes to the same depth
            if height[u] < height[v]:
                u, v = v, u # Ensure u is the deeper node

            k_diff = height[u] - height[v]
            # Lift u up by k_diff steps using binary lifting
            # Iterate through bits of k_diff (from least to most significant)
            j_lift = 0
            while k_diff > 0:
                if (k_diff & 1): # If j_lift-th bit of k_diff is set
                    u = dp[u][j_lift]
                k_diff >>= 1
                j_lift += 1

            # If after lifting, they are the same node, that's the LCA
            if u == v:
                return u

            # Step 2: Lift both nodes simultaneously until their parents are the LCA
            # Iterate from largest jumps downwards.
            # Using MAX_LOG-1 ensures we check all precomputed levels.
            for j in range(MAX_LOG - 1, -1, -1):
                # If their 2^j-th ancestors are different,
                # it means the LCA is further up, so we can jump both nodes
                # Ensure up[u][j] and up[v][j] are not 0 (meaning valid ancestors exist)
                # and that they are indeed different
                if dp[u][j] != dp[v][j]:
                    u = dp[u][j]
                    v = dp[v][j]

            # After the loop, u and v are now direct children of the LCA.
            # So, their parent (dp[u][0]) is the LCA.
            return dp[u][0]

        # Initial DFS call from root 0. Parent of root 0 is 0 itself.
        # This makes dp[0][0] = 0, which is standard for binary lifting roots.
        dfs(0, 0) 

        def calc_dist(u, v):
            a = lca(u, v)
            return dist[u] + dist[v] - 2 * dist[a]

        res = [0] * len(queries)
        for idx, (src1, src2, dest) in enumerate(queries):
            res[idx] = (
                calc_dist(src1, src2) + calc_dist(src2, dest) + calc_dist(dest, src1)
            ) // 2
        return res