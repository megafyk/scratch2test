class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # array
        # time O(nlog(num)), space O(1)
        def sum_d(num):
            s = str(num)
            total = 0
            for d in s:
                total += int(d)
            return total
        
        for idx, num in enumerate(nums):
            if idx == sum_d(num):
                return idx
        return -1