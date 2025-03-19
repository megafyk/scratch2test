class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # bitwise + greedy
        # time O(N), space O(1)
        res = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if i >= n-2:
                    return -1
                nums[i] = 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                res += 1
        return res