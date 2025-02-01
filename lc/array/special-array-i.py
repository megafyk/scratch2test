class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # array
        # time O(n), space O(1)
        isodd = (nums[0] % 2 == 1)
        for i in range(1, len(nums)):
            if (nums[i] % 2 == 1) == isodd:
                return False
            isodd = not isodd 
        return True
        