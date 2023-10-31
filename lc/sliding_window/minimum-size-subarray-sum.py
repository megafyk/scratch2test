from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        slow, fast = 0, 0
        win_sum = 0
        ans = len(nums) + 1
        while fast < len(nums):
            win_sum += nums[fast]
            while win_sum >= target:
                if fast - slow + 1 < ans:
                    ans = fast - slow + 1
                win_sum -= nums[slow]
                slow += 1
            fast += 1
        if ans == len(nums) + 1:
            return 0
        return ans


s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1,1]))
