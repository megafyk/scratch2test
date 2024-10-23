from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        print(arr)
        n = len(arr)
        mx = max(arr[:k])
        dp = [mx*(i+1) if i < k else 0 for i in range(n)]
        dp[0] = arr[0]
        for i in range(k, n):
            for j in range(i-k, i):
                print(max(arr[j+1:i+1]))
                dp[i] = max(dp[i], dp[j] + max(arr[j+1:i+1]) * (i-j))
        print(dp)
        return dp[-1]

arr = [1,15,7,9]
s = Solution()
print(s.maxSumAfterPartitioning(arr, 3))