class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        # knapsack
        # time O(n), space O(n)
        n = len(arr)
        dp = [1] * n
        dic = {arr[0]: 0}
        for i in range(1, n):
            num = arr[i] - diff
            if num in dic:
                dp[i] = dp[dic[num]] + 1
            dic[arr[i]] = i
        return max(dp)