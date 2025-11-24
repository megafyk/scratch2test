class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        res = [False] * n
        cur = 0
        for i in range(n):
            cur = (cur << 1) | nums[i]
            if cur % 5 == 0:
                res[i] = True
        return res