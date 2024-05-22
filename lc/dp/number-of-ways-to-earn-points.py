class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        mod = pow(10, 9) + 7
        for i in range(1, n+1):
            count, mark = types[i-1]
            for j in range(target+1):
                for cnt in range(count+1):
                    if j >= cnt * mark:
                        dp[i][j] += dp[i-1][j-cnt*mark]
                        dp[i][j] %= mod
        return dp[-1][-1]