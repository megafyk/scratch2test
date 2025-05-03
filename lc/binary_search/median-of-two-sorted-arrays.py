class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)
        l,r = 0, len1 - 1

        while True:
            m1 = l + (r - l) // 2 if l <= r else -1 # mid idx nums1
            m2 = half - m1 - 2 # mid idx nums2

            nums1_l = nums1[m1] if m1 >= 0 else -sys.maxsize
            nums1_r = nums1[m1 + 1] if m1 + 1 < len1 else sys.maxsize

            nums2_l = nums2[m2] if m2 >= 0 else -sys.maxsize
            nums2_r = nums2[m2 + 1] if m2 + 1 < len2 else sys.maxsize

            if nums1_l <= nums2_r and nums2_l <= nums1_r:
                if total % 2:
                    return min(nums1_r, nums2_r) # Corrected: Should be min of the right sides
                return (max(nums1_l, nums2_l) + min(nums1_r, nums2_r)) / 2
            elif nums1_l > nums2_r:
                r = m1 - 1
            else:
                l = m1 + 1