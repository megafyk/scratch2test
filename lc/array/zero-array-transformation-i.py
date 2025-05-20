class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # prefix sum
        # time O(n+q), space O(n)
        n = len(nums)
        delta_log = [0] * n # log tracking
        for start,end in queries:
            delta_log[start] += 1
            if end < n-1: delta_log[end+1] -= 1
        prefix = [0] * n
        prefix[0] = delta_log[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + delta_log[i]
        for i in range(n):
            if nums[i] > prefix[i]:
                return False
        return True