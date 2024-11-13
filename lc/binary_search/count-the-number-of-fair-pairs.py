class Solution:
    def bin_search(self, nums, target, l, r):
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # binary search
        # time O(nlogn), space O(n)
        n = len(nums)
        nums = sorted(nums)
        res = 0
        for i in range(n):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (self.bin_search(nums, up, i+1, n) - self.bin_search(nums, low-1, i+1, n))
        return res
