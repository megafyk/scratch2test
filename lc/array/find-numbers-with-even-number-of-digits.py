class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # time O(N), space O(1)
        res = 0
        for num in nums:
            if 10 <= num <= 99 or 1000 <= num <= 9999 or num == 100000:
                res += 1
        return res