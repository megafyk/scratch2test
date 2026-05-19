class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # time O(min(m,n)), space O(1)
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1
