class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time O(n), space O(n)
        idx = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in idx:
                return [idx[t], i]
            idx[nums[i]] = i
        return []