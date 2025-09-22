class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(i):
                k = nums[i] - nums[j]
                dp[(i,k)] = max(dp[(i,k)], dp[(j,k)] + 1 if (j,k) in dp else 2)
                res = max(res, dp[(i,k)])
        return res