class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp kadane's algorithm
        # time O(n), space O(1)
        prefix, suffix = 0,0
        mx = -10 ** 9 + 7
        n = len(nums)
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n-i-1]
            mx = max(mx, prefix, suffix)
        return mx
    
class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        # array
        # time O(n), space O(1)
        n = len(nums)
        neg_prod = 1
        cur = 1
        res = nums[0]
        for i in range(n):
            if nums[i] != 0:
                cur *= nums[i]
                if cur < 0:
                    if neg_prod == 1:
                        neg_prod = cur
                    else:
                        if nums[i] < 0:
                            res = max(res, cur // nums[i])
                        res = max(res, cur // neg_prod)
                res = max(res, cur)
            else:
                neg_prod = 1
                cur = 1
                res = max(res, 0)
        
        return res