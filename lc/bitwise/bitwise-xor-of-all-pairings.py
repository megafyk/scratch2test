class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # bitwise
        # time O(m+n), space O(1)
        m = len(nums1)
        n = len(nums2)
        
        res = 0
        for a in nums1: 
            if n % 2 == 1: # a repeat n times
                res ^= a
        for b in nums2:
            if m % 2 == 1: # b repeat m times
                res ^= b

        return res
