class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            r = num % 3
            if r != 0: res += 1
        return res