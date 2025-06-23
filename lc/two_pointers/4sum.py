from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        def ksum(k, nums: List[int], target) -> List[List[int]]:

            if k == 2:
                res = []
                idx1 = 0
                idx2 = len(nums) - 1
                while idx1 < idx2:
                    if nums[idx1] + nums[idx2] > target:
                        idx2 -= 1
                    elif nums[idx1] + nums[idx2] < target:
                        idx1 += 1
                    else:
                        if [nums[idx1], nums[idx2]] not in res:
                            res.append([nums[idx1], nums[idx2]])
                        idx1 += 1
                        idx2 -= 1
                return res

            res = []
            for i in range(len(nums)):
                tmp = ksum(k - 1, nums[i + 1:], target - nums[i])
                for j in range(len(tmp)):
                    if [nums[i]] + tmp[j] not in res:
                        res.append([nums[i]] + tmp[j])
            return res

        return ksum(4, nums, target)


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
