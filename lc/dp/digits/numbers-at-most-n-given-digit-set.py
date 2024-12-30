class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # dp digits
        # time O(log(N)), space O(log(N))
        d_len = len(digits)
        n_str = str(n)
        n_len = len(n_str)

        cnt = 0
        # len num < n_len
        for i in range(1, n_len):
            cnt += d_len ** i

        dp = [0] * n_len
        # len num == n_len
        for i in range(n_len-1, -1, -1):
            for d in digits:
                if d < n_str[i]:
                    dp[i] += d_len ** (n_len-i-1)
                elif d == n_str[i]:
                    dp[i] += dp[i+1] if i < n_len-1 else 1

        return cnt + dp[0]
