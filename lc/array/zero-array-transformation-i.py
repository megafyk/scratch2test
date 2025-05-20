class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # prefix sum
        # time O(n+q), space O(n)
        n = len(nums)
        delta_log = [0] * (n+1) # log tracking
        for start,end in queries:
            delta_log[start] += 1
            delta_log[end+1] -= 1
        
        cur = 0
        
        for i in range(n):
            cur += delta_log[i]
            if nums[i] > cur:
                return False
        return True