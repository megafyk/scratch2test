class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)
        for u,v in hierarchy:
            adj[u-1].append(v-1)

        def merge(A,B):
            C = [-sys.maxsize] * len(A)
            for i in range(len(A)):
                for j in range(len(A) - i):
                    C[i+j] = max(C[i+j], A[i]+B[j])

            return C

        def dfs(u):
            dp0 = [0] * (budget+1) # dp0[b] => max profit for budget b with no discount
            dp1 = [0] * (budget+1) # dp1[b] => max profit for budget b with discount
            for v in adj[u]:
                res0,res1 = dfs(v) 
                dp0,dp1 = merge(res0, dp0), merge(res1, dp1)

            ans0 = list(dp0)
            ans1 = list(dp0)

            cost = present[u]
            for b in range(cost, budget+1):
                ans0[b] = max(ans0[b], dp1[b-cost] + future[u] - cost)
            
            cost //= 2
            for b in range(cost, budget+1):
                ans1[b] = max(ans1[b], dp1[b-cost] + future[u] - cost)

            return ans0,ans1

        return max(dfs(0)[0])
