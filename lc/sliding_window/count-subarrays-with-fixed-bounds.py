class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # sliding window
        # time O(N), space O(1)
        N = len(nums)
        res = 0
        jmin = jmax = jbad = -1
        for i,num in enumerate(nums):
            if num < minK or num > maxK: jbad = i
            if num == minK: jmin = i
            if num == maxK: jmax = i
            res += max(0, min(jmin, jmax) - jbad)
        return res 