class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # math combinatorics
        res = 0
        for num in nums:
            res |= num
        return res  * 2 ** (len(nums) - 1)

    # def subsetXORSum(self, nums: List[int]) -> int:
    #     # backtrack
    #     # time O(2^N), space O(N)
        
    #     def backtrack(start, cur):
    #         if start == len(nums):
    #             return 0

    #         total = 0
    #         for i in range(start, len(nums)):
    #             cur ^= nums[i]
    #             total += cur
    #             total += backtrack(i+1, cur)
    #             cur ^= nums[i]
    #         return total

    #     return backtrack(0,0)