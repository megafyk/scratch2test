class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        suffix = [sys.maxsize] * n
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = min(suffix[i+1], nums[i])
        score = -sys.maxsize
        for i in range(n-1):
            score = max(score, prefix[i] - suffix[i+1])
        return score