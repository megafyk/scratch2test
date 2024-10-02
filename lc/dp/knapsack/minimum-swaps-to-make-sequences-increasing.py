class Solution:

    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # dp knapsack
        # complexity: time O(n), space O(1)
        n = len(nums1)

        # swap = [0] * n
        # no_swap = [0] * n

        swap = 1
        no_swap = 0

        for i in range(1, n):
            swap2 = sys.maxsize
            no_swap2 = sys.maxsize
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                # no_swap[i] = no_swap[i - 1]
                # swap[i] = swap[i - 1] + 1
                no_swap2 = no_swap
                swap2 = swap + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                # swap[i] = min(swap[i], no_swap[i - 1] + 1)
                # no_swap[i] = min(no_swap[i], swap[i - 1])
                swap2 = min(swap2, no_swap + 1)
                no_swap2 = min(no_swap2, swap)
            swap = swap2
            no_swap = no_swap2

        return min(swap, no_swap)
