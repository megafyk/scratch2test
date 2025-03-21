class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bitwise XOR
        # time O(N), space O(1)
        res = 0
        for num in nums:
            res ^= num
        return res