class Solution:

    # def distributeCandies(self, n: int, limit: int) -> int:
    #     # time O(N), space O(1)
    #     res = 0
    #     for i in range(0, min(limit, n) + 1):
    #         if n - i <= 2 * limit:
    #             res += min(n-i, limit) - max(0, n-i-limit) + 1
    #     return res
    def distributeCandies(self, n: int, limit: int) -> int:
        # combinatoric contraction
        # time O(1), space O(1)
        def calc(x):
            if x <= 0:
                return 0
            return x * (x - 1) // 2

        return (
            calc(n + 2)
            - 3 * calc(n - (limit + 1) + 2)
            + 3 * calc(n - 2 * (limit + 1) + 2)
            - calc(n - 3 * (limit + 1) + 2)
        )
