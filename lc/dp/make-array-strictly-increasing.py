class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # dp hard
        # time O(mnlog(n)), space O(n)
        arr2 = sorted(arr2)
        n = len(arr2)
        dp = {-1: 0}

        for i in range(len(arr1)):
            new_dp = defaultdict(lambda: sys.maxsize)
            for prev in dp:
                # not replace dp[i]
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                # replace dp[i]
                idx = bisect.bisect(arr2, prev)
                if idx < n:
                    new_dp[arr2[idx]] = min(new_dp[arr2[idx]], dp[prev] + 1)
            dp = new_dp

        return min(dp.values()) if dp else -1
