class Solution:
    def divide(self, nums, maxop, max_balls):
        op = 0
        for num in nums:
            op += math.ceil(num / max_balls) - 1
            if op > maxop: return False
        return True

    def minimumSize(self, nums: List[int], maxop: int) -> int:
        # binary search -> maximum bags by find minimum balls
        # time O(n + nlogn), space O(1)
        l, r = 1, max(nums)
        while l < r:
            mid = l + (r -l) // 2
            if self.divide(nums, maxop, mid):
                r = mid
            else:
                l = mid + 1
        return l
