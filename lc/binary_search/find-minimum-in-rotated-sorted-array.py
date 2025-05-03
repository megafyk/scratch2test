class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # time O(log(N)), space O(1) 
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]