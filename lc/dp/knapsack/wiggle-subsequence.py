class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        # dp knapsack
        # time O(n), space O(1)
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                down = up + 1
            elif nums[i] < nums[i-1]:
                up = down + 1
        return max(up, down)


    # def fillmax(self, dp, posi, nums):
    #     n = len(nums)
    #     start = 0
    #     for i in range(2, n+1):
    #         numi = nums[i-1]
    #         toggle = False
    #         for j in range(start, i):
    #             numj = nums[j-1]
    #             if (posi and numi-numj > 0) or (not posi and numi-numj <0):
    #                 if dp[j] + 1 > dp[i]:
    #                     dp[i] = dp[j] + 1
    #                     start = i    
    #                 toggle = True
    #             else:
    #                 if dp[j] > dp[i]:
    #                     dp[i] = dp[j]
    #                     start = i
    #                 toggle = False
    #         posi = not posi if toggle else posi

    # def wiggleMaxLength(self, nums: List[int]) -> int:
    #     # dp knapsack positive start dp and negative start dp
    #     # time O(n^2), space O(n)
    #     n = len(nums)
    #     dp1 = [0] * (n+1)
    #     dp2 = [0] * (n+1)
    #     dp1[1] = dp2[1] = 1
        
    #     self.fillmax(dp1, True, nums)
    #     self.fillmax(dp2, False, nums)
    #     return max(dp1[-1], dp2[-1])
