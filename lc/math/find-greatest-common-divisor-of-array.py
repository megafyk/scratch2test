class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx, mi = max(nums), min(nums)
        return gcd(mx, mi)
