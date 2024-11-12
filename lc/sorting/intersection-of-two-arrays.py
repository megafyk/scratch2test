class Solution:

    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # complexity: time O(n+m), mem O(n+m)
    #     n = len(nums1)
    #     m = len(nums2)
    #     s1 = set()
    #     for i in range(n):
    #         s1.add(nums1[i])
    #     s = set()
    #     for j in range(m):
    #         if nums2[j] in s1:
    #             s.add(nums2[j])
    #     return list(s)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # complexity: time O(nlogn + mlogm + n + m), mem O(1)
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        n = len(nums1)
        m = len(nums2)

        j = 0
        s = set()
        for i in range(n):
            while j < m - 1 and nums1[i] > nums2[j]:
                j+=1
            if nums1[i] < nums2[j]:
                continue
            elif nums1[i] == nums2[j]:
                s.add(nums1[i])

        return list(s)
            