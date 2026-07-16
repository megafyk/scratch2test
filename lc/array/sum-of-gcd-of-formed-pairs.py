class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        # array
        # time O(nlogn), space O(1)
        mx = nums[0]
        n = len(nums)
        for i, num in enumerate(nums):
            mx = max(mx, num)
            nums[i] = gcd(num, mx)
        nums.sort()
        res = 0

        for i in range(n//2):
            res += gcd(nums[i], nums[n-i-1])
        return res
