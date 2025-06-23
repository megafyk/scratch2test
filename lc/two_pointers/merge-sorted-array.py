from typing import List


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


s = Solution()
t1 = [4, 5, 6, 0, 0, 0]
t2 = [1, 2, 3]
s.merge(t1, 3, t2, 3)
print(t1)
