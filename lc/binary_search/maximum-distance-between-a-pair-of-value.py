class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # 2 pointers
        # time O(m), space O(1)
        n,m = len(nums1), len(nums2)
        i = 0
        for j in range(m):
            if nums2[j] < nums1[i]:
                i += 1
                if i >= n:
                    break
        return max(j-i, 0)

class Solution1:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # binary search
        # n = len(nums1), m = len(nums2)
        # time O(nlogm), space O(1)
        mx_dist = -1
        for i, num in enumerate(nums1):
            m = len(nums2)
            l, r = i, m - 1
            while l < r:
                mid = l + (r-l+1) // 2
                if nums2[mid] >= nums1[i]:
                    l = mid
                else:
                    r = mid - 1
            mx_dist = max(mx_dist, l-i)
        return mx_dist