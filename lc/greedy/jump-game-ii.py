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
        
        # greedy approach, complexity O(n), mem O(1)
        n = len(nums)
        idx_cur = 0
        idx_nxt = 0
        cnt = 0

        while idx_cur < n - 1:
            idx_nxt = idx_cur
            for j in range(idx_cur, idx_cur + nums[idx_cur] + 1):
                if j < n-1 and j + nums[j] >= idx_nxt + nums[idx_nxt]:
                    # update new target idx_nxt
                    idx_nxt = j

            print(idx_cur, idx_nxt, idx_cur + nums[idx_cur], n - 1)
            if idx_cur + nums[idx_cur] >= n - 1:
                idx_cur = n
            else:
                idx_cur = idx_nxt
            print(idx_cur, idx_nxt)
            cnt += 1
            

        return cnt