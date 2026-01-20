class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        mi = defaultdict(int)
        for i in range(1, max(nums)+1):
            t = i | (i+1)
            if t not in mi:
                mi[t] = i

        n = len(nums)
        res = [-1] * n
        for i in range(n):
            if nums[i] in mi:
                res[i] = mi[nums[i]]
        return res