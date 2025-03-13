class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # binary search + prefix sum
        # time O(NlogN), space O(N)
        N = len(nums)
        Q = len(queries)
        left = 0
        right = Q + 1

        def check(target):
            # trick query range [l, r]
            diff = [0] * (N + 1)

            for l,r,v in queries[:target]:
                diff[l] += v
                diff[r+1] -= v
            
            cur = 0
            for i in range(N):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True
        
        while left < right:
            mid = left + (right-left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        if left  > Q: return -1
        return left