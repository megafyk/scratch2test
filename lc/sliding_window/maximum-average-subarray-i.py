class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = -10000
        msum = cur_sum = sum(nums[:k])
        n = len(nums)
        for i in range(k, n):
            cur_sum = cur_sum + nums[i] - nums[i-k]
            msum = max(msum, cur_sum)
        return msum / k