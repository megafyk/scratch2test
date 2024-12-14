class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # dp distinct ways
        # time O(n^2), space O(n)
        n = len(nums)
        nums = sorted(nums)
        dp = [1] * n
        path = [[nums[i]] for i in range(n)]

        res = [nums[0]]

        mx = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        path[i] = list(path[j])
                        path[i].append(nums[i])
                        if len(path[i]) > mx:
                            mx = len(path[i])
                            res = path[i]
        return res
