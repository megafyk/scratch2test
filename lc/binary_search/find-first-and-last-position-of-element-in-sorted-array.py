class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # time O(logn), space O(1)
        if not nums:
            return [-1, -1]
        
        first = self.search(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        
        last = self.search(nums, target + 1) - 1
        return [first, last]
