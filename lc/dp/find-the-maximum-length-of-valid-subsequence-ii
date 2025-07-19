class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp with math
        # time O(n*k), space O(k)
        n = len(nums)
        res = 0
        for i in range(k):
            dp = [0] * k
            for a in nums:
                cur = a % k
                prev = (i - cur + k) % k
                dp[cur] = max(dp[cur], dp[prev] + 1)
                res = max(res, dp[cur])
        return res

class Solution1:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp with math
        # time O(n*k), space O(k*k)
        n = len(nums)
        dp = [[0] * k for _ in range(k)] # dp[a][b] => length of subsequence end with ..a,b
        res = 0
        for a in nums:
            for b in range(k):
                dp[b][a%k] = max(dp[b][a%k], dp[a%k][b] + 1)
                res = max(res, dp[b][a%k])
        return res