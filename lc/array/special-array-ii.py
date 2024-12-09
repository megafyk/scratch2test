class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # prefix sum
        # time O(n), space O(n)
        n = len(nums)
        prefix = [1] * n
        for i in range(1, n):
            if (nums[i] % 2 == 0 and nums[i-1] % 2 == 1) or (nums[i] % 2 == 1 and nums[i-1] % 2 == 0):
                prefix[i] = prefix[i-1] + 1
        res = [False] * len(queries)
        for idx, (s,e) in enumerate(queries):
            if e - s == prefix[e] - prefix[s]:
                res[idx] = True
        return res
