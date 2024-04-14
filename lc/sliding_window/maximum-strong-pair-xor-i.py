class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # complexity O(n^2)
        nums = sorted(nums)
        res = 0
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] - nums[i] > nums[i]:
                    break
                res = max(res, nums[j] ^ nums[i])
        return res