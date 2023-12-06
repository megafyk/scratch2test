from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]] += 1

        def helper(res):
            if len(res) == len(nums):
                ans.append(res)
                return

            for k in freq:
                if freq[k] == 0:
                    continue
                freq[k] -= 1
                helper(res + [k])
                freq[k] += 1

        helper([])

        return ans


s = Solution()
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 2, 3]))
