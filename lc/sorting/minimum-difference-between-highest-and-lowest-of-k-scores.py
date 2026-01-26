class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mi = sys.maxsize
        for i in range(n-k+1):
            mi = min(mi, nums[i+k-1] - nums[i])
        return mi