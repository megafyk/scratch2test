class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # dp bitwise
        # time O(n), space O(n)
        s = set()
        endwith = set()
        for num in arr:
            endwith = {num | i for i in endwith}
            endwith.add(num)
            s |= endwith
        return len(s)

    # def subarrayBitwiseORs(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     s = set()
    #     dp = [[0] * (n+1) for _ in range(n)]
    #     for i in range(n):
    #         dp[i][i] = arr[i]

    #     for i in range(n):
    #         for j in range(i+1, n+1):
    #             dp[i][j] = dp[i][j-1] | arr[j-1]
    #             s.add(dp[i][j])

    #     return len(s)
