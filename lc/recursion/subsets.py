from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        ans = [[]]

        for i in range(len(nums)):
            tmp_set = [nums[i]]
            smaller_nums = nums[i + 1 :]

            for sub in self.subsets(smaller_nums):
                ans.append(tmp_set + sub)

        return ans


s = Solution()
print(s.subsets([1, 2, 3]))
