class Solution:
    def findIntegers(self, n: int) -> int:
        # dp digits
        # time O(log(n)), space O(log(n))
        binary = bin(n)[2:]
        m = len(binary)
        dp = [[0] * 2 for _ in range(m + 1)]
        dp[1][1] = dp[1][0] = 1
        for i in range(2, m + 1):
            dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
            dp[i][1] = dp[i - 1][0]

        last_bit = "0"
        res = 0

        for i in range(m):
            if binary[i] == "1":
                res += dp[m - i][0]
                if last_bit == "1":
                    return res
            last_bit = binary[i]

        return res + 1
