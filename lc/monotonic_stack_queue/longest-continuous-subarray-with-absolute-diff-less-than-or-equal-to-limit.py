from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incr = deque()
        decr = deque()
        n = len(nums)
        begin = 0

        res = 0
        for end, num in enumerate(nums):
            while incr and num < incr[-1]:
                incr.pop()
            incr.append(num)
            while decr and num > decr[-1]:
                decr.pop()
            decr.append(num)

            while decr[0] - incr[0] > limit:
                if decr[0] == nums[begin]:
                    decr.popleft()

                if incr[0] == nums[begin]:
                    incr.popleft()
            
                begin += 1

            res = max(res, end - begin + 1)
        
        return res