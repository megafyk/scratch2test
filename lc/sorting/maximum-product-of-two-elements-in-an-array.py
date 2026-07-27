class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sorting
        # time O(n), space O(1)
        mx1,mx2 = 0,0
        for n in nums:
            if n >= mx2:
                mx1 = mx2
                mx2 = n
            elif mx1 < n < mx2:
                mx1 = n
        return (mx1-1) * (mx2-1)
