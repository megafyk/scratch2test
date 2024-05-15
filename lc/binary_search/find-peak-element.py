class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # basic binary search
        # complexity: time O(logn), mem O(1)
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        return l