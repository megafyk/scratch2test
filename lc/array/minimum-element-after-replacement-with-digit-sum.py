class Solution:
    def minElement(self, nums: List[int]) -> int:
        # array
        # time O(nlogd), space O(1)
        mi_d_sum = inf
        for num in nums:
            d_sum = 0
            while num > 0:
                d_sum += num % 10
                num //= 10
            mi_d_sum = min(mi_d_sum, d_sum)
        return mi_d_sum
