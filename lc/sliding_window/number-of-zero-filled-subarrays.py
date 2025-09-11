class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # sliding window
        # time O(n), space O(1)
        res = 0
        cnt_0 = 0
        for num in nums:
            if num == 0:
                cnt_0 += 1
                res += cnt_0
            else:
                cnt_0 = 0
        return res