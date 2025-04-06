class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # dp distinct ways
        # time O(NlogN + N^2), space O(N + N^2)

        n = len(nums)
        nums = sorted(nums)
        dp = [1] * n
        path = [[num] for num in nums]
        res = path[0]
        mx_len = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        path[i] = list(path[j])
                        path[i].append(nums[i])
                        if len(path[i]) > mx_len:
                            mx_len = len(path[i])
                            res = path[i]
        return res