class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # brute force
        # time O(n * log10(m)), space O(n * log10(m)), m is the max number in nums
        res = []
        for num in nums:
            tmp = []
            while num > 0:
                tmp.append(num % 10)
                num //= 10
            res += tmp[::-1]

        return res
