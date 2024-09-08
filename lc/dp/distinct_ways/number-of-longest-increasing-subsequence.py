class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp distinct ways
        # complexity: time O(n^2), mem O(n)
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n
        lis = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = 0
                    if dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            lis = max(lis, dp[i])
        res = 0
        for i in range(n):
            if dp[i] == lis:
                res += cnt[i]
        return res
