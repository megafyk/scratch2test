class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # array
        # time O(n), space O(n)
        n = len(nums)
        res = []
        for i in range(n):
            res.append(nums[(i + n + nums[i]) % n])
        return res