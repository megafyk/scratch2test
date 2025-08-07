class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # dp on matrix
        # time O(n^2), space O(n)
        
        n = len(fruits)
        res = 0
        res += sum([fruits[i][i] for i in range(n)])

        def get_max():
            dp = [0] * (n + 1)
            for i in range(n - 1):
                nw_dp = [0] * (n + 1)
                for j in range(max(i + 1, n - 1 - i), n):
                    nw_dp[j] = max(dp[j-1], dp[j], dp[j+1])
                    nw_dp[j] += fruits[i][j]
                dp = nw_dp
            return dp[-2]

        # start from (0,n-1)
        res += get_max()
        # transpose
        for i in range(n):
            for j in range(i):
                fruits[i][j], fruits[j][i] = fruits[j][i], fruits[i][j]
        # start from (n-1, 0)
        print(fruits)
        res += get_max()
        return res
