from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp approach, complexity O(n^2), mem O(n)
        # n = len(nums)
        # dp = [n] * n
        # dp[0] = 0

        # for i in range(n):
        #     for j in range(1, nums[i] + 1):
        #         nxt_idx = j + i
        #         if nxt_idx < n:
        #             dp[nxt_idx] = min(dp[nxt_idx], dp[i] + 1)

        # return dp[n-1] if dp[n-1] != n else -1
        return -1
