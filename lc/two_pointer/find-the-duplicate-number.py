from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0
        while slow != fast or fast == 0:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


s = Solution()
print(s.findDuplicate([3, 1, 3, 4, 2]))
