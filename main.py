import sys

class Solution:
    def min_cost(self, cost, pair_cost, k):
        # dp interval
        # time O(n*n*k), space O(n*n)
        n = len(cost) 
        k = min(k, n//2)
        dp = [[[sys.maxsize] * n for _ in range(n)] for _ in range(2)]

        # base case
        for i in range(n):
            dp[0][i][i] = cost[i]
            dp[1][i][i] = cost[i]

        for kk in range(k+1):
            cur = kk % 2
            prev = (kk - 1) % 2
            for length in range(2, n+1):
                for i in range(n-length+1):
                    j = i + length - 1
                    mi = min(cost[i] + dp[cur][i+1][j], cost[j] + dp[cur][i][j-1])
                    
                    if kk > 0:
                        mi = min(mi, pair_cost + dp[prev][i+1][j-1])
                    dp[cur][i][j] = mi
        return dp[k%2][0][n-1]

if __name__ == "__main__":
    s = Solution()
    cost = [8,2,9,4]
    pair_cost = 10
    k = 1
    print(s.min_cost(cost, pair_cost, k))