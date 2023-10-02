from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = set()
        nums.sort()
        for i in range(len(nums) - 2):
            idx1 = i + 1
            idx2 = len(nums) - 1

            while idx1 < idx2:
                if nums[idx1] + nums[idx2] > -nums[i]:
                    idx2 -= 1
                elif nums[idx1] + nums[idx2] < -nums[i]:
                    idx1 += 1
                else:
                    a.add((nums[i], nums[idx1], nums[idx2]))
                    idx1 += 1
                    idx2 -= 1

        return [list(t) for t in a]


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
