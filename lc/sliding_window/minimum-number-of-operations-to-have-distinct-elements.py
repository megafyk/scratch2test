class Solution:
    def minOperations(self, nums: List[int]) -> int:
        first = {}
        res = 0
        for i,num in enumerate(nums):
            if num in first:
                idx = first[num]
                res = max(res, math.ceil((idx+1)/3))
            first[num] = i
        return res