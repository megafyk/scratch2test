class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # dp matrix multiplication + matrix exponentiation
        # dp[i][j] = number of ways to transform i to j
        # time complexity: O(26^3 * log(t))
        # space complexity: O(26^2)
        mod = 10 ** 9 + 7
        def multiply(A,B):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % mod
            return res
        
        def pow(matrix, n):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                res[i][i] = 1

            while n:
                if n % 2 == 1: res = multiply(res, matrix)
                matrix = multiply(matrix, matrix)
                n = n >> 1
            return res

        cnt = [0] * 26
        for c in s: cnt[ord(c) - ord('a')] += 1

        # matrix[i][j] = 1 => after 1 transformation, i can be transformed to 1 character j
        matrix = [[0] * 26 for _ in range(26)]

        for i in range(26):
            for j in range(1, nums[i] + 1):
                matrix[(i+j) % 26][i] = 1

        matrix = pow(matrix, t)

        res = [0] * 26
        for i in range(26):
            for j in range(26):
                res[i] = (res[i] + matrix[i][j] * cnt[j]) % mod

        return sum(res) % mod
        