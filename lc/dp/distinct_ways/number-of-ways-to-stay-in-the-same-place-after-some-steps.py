class Solution:
    # def dp(self, remain, idx, memo, arrLen):
    #     if idx < 0 or idx >= arrLen: return 0
    #     if idx > remain: return 0
    #     if remain == 0:
    #         if idx == 0:
    #             return 1
    #         return 0
    #     if (remain, idx) in memo: return memo[(remain, idx)]
    #     res = 0
    #     res += self.dp(remain-1, idx-1, memo, arrLen)
    #     res += self.dp(remain-1, idx, memo, arrLen)
    #     res += self.dp(remain-1, idx+1, memo, arrLen)
    #     memo[(remain, idx)] = res
    #     return res
        
    # def numWays(self, steps: int, arrLen: int) -> int:
    #     # complexity: time O(step^2), space O(step^2)
    #     memo = {}
    #     mod = 10 ** 9 + 7
    #     return self.dp(steps,0,memo, arrLen) % mod
    
    def numWays(self, steps: int, arrLen: int) -> int:
        # complexity: time O(steps^2), mem O(steps)
        mod = 10 ** 9 + 7
        dp = [0] * min(steps // 2 + 1, arrLen)
        dp[0] = 1
        for i in range(steps):
            newdp = [0] * min(steps // 2 + 1, arrLen)
            for j, ways in enumerate(dp):
                if ways > 0:
                    for dx in (-1,0,1):
                        idx = j + dx
                        if idx < 0 or idx >= len(dp): continue
                        newdp[idx] += ways
                        newdp[idx] %= mod
            dp = newdp
        return dp[0]
