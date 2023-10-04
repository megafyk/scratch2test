from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1

        for i in range(len(numbers)):
            if numbers[idx1] + numbers[idx2] < target:
                idx1 += 1
            elif numbers[idx1] + numbers[idx2] > target:
                idx2 -= 1
            else:
                return [idx1 + 1, idx2 + 1]

s= Solution()
print(s.twoSum([2,7,11,15], 9))
