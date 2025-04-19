class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # binary search
        # time O(NlogN), space O(1)
        def search(target, l, r):
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l

        N = len(nums)
        nums = sorted(nums)
        res = 0
        for i in range(N):
            low = lower - nums[i]
            up = upper - nums[i]
            res += search(up, i+1, N) - search(low-1, i+1, N)
        return res