class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # array
        # time O(N), space O(1)
        N = len(nums)
        for i in range(N):
            nums[i] = nums[i] + N * (nums[nums[i]] % N) # euclid encode a = bq + r (a = nums[nums[i]], b = nums[i])
        for i in range(N):
            nums[i] = nums[i] // N
        return nums
    
# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         return [nums[nums[i]] for i in range(len(nums))]
