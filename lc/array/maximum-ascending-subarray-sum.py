class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # array
        # time O(n), space O(1)
        res = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                cur_sum = 0
            cur_sum += nums[i]
            res = max(res, cur_sum)

        return res
        