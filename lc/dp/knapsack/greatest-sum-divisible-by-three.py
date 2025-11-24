class Solution:
    def assign(self, t, dp):
        if t % 3 == 0:
            dp[0] = max(dp[0], t)
        elif t % 3 == 1:
            dp[1] = max(dp[1], t)
        else:
            dp[2] = max(dp[2], t)
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp mod knapsack 3k,3k+1,3k+2
        # time O(n), space O(1)
        dp = [0] * 3
        for num in nums:
            t0 = dp[0] + num
            t1 = dp[1] + num
            t2 = dp[2] + num
            self.assign(t0, dp)
            self.assign(t1, dp)
            self.assign(t2, dp)
        return dp[0]

class Solution1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        min1 = min11 = min2 = min22 = sys.maxsize
        for i in range(n):
            total += nums[i]
            r = nums[i] % 3
            if r == 1:
                if nums[i] < min1:
                    min1, min11 = nums[i], min1
                elif nums[i] < min11:
                    min11 = nums[i]
            elif r == 2:
                if nums[i] < min2:
                    min2, min22 = nums[i], min2
                elif nums[i] < min22:
                    min22 = nums[i]
                    
        r = total % 3
        if r == 1:
            return max(total - min1, total - (min2 + min22))
        elif r == 2:
            return max(total - min2, total - (min1 + min11))
        else:
            return total
                    
