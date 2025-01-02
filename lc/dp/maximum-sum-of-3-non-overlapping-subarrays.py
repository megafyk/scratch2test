class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # dp array + sliding window
        # time O(n), space O(n)
        n = len(nums)
        presum = [sum(nums[:k])]
        for i in range(k, n):
            presum.append(presum[-1] - nums[i - k] + nums[i])

        dp = {}
        def max_sum(idx, cnt):
            if cnt == 3 or idx > n - k:
                return 0
            if (idx, cnt) in dp: return dp[(idx, cnt)]
            include = presum[idx] + max_sum(idx+k, cnt+1)
            skip = max_sum(idx+1, cnt)

            dp[(idx, cnt)] = max(include, skip)
            return dp[(idx, cnt)]

        res = []

        i = 0
        while i <= n-k and len(res) < 3:
            include = presum[i] + max_sum(i+k, len(res) + 1)
            skip = max_sum(i+1, len(res))

            if include >= skip:
                res.append(i)
                i+=k
            else:
                i += 1

        return res
