class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # bitwise
        # time O(N), space O(1)
        n = len(nums)
        res = 0
        for i in range(n+1):
            res ^= i

        for num in nums:
            res ^= num
        return res