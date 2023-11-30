from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        ans = []

        for i in range(len(nums)):
            smaller_nums = nums[:i] + nums[i + 1 :]
            perm_smaller_nums = self.permute(smaller_nums)
            for p in perm_smaller_nums:
                ans.append([nums[i]] + p)

        return ans


s = Solution()
print(s.permute([1, 2, 3]))
