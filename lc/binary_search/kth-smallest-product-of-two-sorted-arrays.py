import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # double binary search
        # time O(n*log(m) * log(m*n)), space O(1)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        def count(prod):
            count = 0
            for a in nums1:
                if a == 0:
                    if prod >= 0:
                        count += len(nums2)
                elif a > 0:
                    count += bisect.bisect_right(nums2, prod // a)
                else:
                    count += len(nums2) - bisect.bisect_left(nums2, ceil(prod / a))
                    

            return count

        l = min(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        )
        r = max(
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        )

        while l < r:
            m = l + (r - l) // 2
            if count(m) >= k:
                r = m
            else:
                l = m + 1
        return l
