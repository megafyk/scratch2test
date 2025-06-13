class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # binary search
        # time O(nlogn), space O(1)
        nums = sorted(nums)
        n = len(nums)
        l, r = 0, abs(nums[-1] - nums[0])

        def enough(m):
            cnt_pairs = 0
            i = 0
            while i < n - 1:
                diff = abs(nums[i+1] - nums[i])
                if diff <= m:
                    i += 1
                    cnt_pairs += 1
                i += 1
            return cnt_pairs >= p

        while l < r:
            m = l + (r - l) // 2
            if enough(m):
                r = m
            else:
                l = m + 1
        return l
