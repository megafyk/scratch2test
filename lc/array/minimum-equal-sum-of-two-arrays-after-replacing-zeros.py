class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # array
        # time O(m+n), space O(1)
        cnt1 = 0
        sum1 = 0
        for n in nums1:
            cnt1 += 1 if n == 0 else 0
            sum1 += n
        cnt2 = 0
        sum2 = 0
        for n in nums2:
            cnt2 += 1 if n == 0 else 0
            sum2 += n
        
        if cnt1 == 0 and cnt2 != 0 and sum2 + cnt2 > sum1:
            return -1
        if cnt2 == 0 and cnt1 != 0 and sum1 + cnt1 > sum2:
            return -1
        if cnt1 == cnt2 == 0 and sum1 != sum2:
            return -1
        
        return max(sum1 + cnt1, sum2 + cnt2)