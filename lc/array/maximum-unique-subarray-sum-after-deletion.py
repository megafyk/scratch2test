class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # array
        # time O(n), space O(n)
        mx = -sys.maxsize        
        s = set()
        for num in nums:
            mx = max(mx, num)
            if num > 0 and num not in s:
                s.add(num)
        if not s: return mx
        return sum(s)