class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # time O(N), space O(1)
        n = len(nums)
        mask = 0
        for i in range(n-1, -1, -1):
            if (mask >> nums[i]) & 1 == 1:
                return i // 3 + 1
            mask |= 1 << nums[i]
        return 0