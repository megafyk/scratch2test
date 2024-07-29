class Solution:

    def numTeams(self, rating: List[int]) -> int:
        # dp
        # complexity: time O(n^2), mem O(1)
        n = len(rating)
        ans = 0
        for i in range(n):
            left_incr = 0
            right_incr = 0

            for j in range(0, i):
                if rating[j] < rating[i]:
                    left_incr += 1

            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    right_incr += 1
            ans += left_incr * right_incr

            left_desc = 0
            right_desc = 0

            for j in range(0, i):
                if rating[j] > rating[i]:
                    left_desc += 1

            for j in range(i + 1, n):
                if rating[i] > rating[j]:
                    right_desc += 1

            ans += left_desc * right_desc

        return ans

    # def dp(self, rating, memo, incr, idx, matched):
    #     if matched == 3:
    #         return 1
    #     if (idx, matched, incr) in memo:
    #         return memo[(idx, matched, incr)]
    #     ans = 0
    #     for i in range(idx + 1, len(rating)):
    #         if (incr and rating[idx] < rating[i]) or (
    #             not incr and rating[idx] > rating[i]
    #         ):
    #             ans += self.dp(rating, memo, incr, i, matched + 1)
    #     memo[(idx, matched, incr)] = ans
    #     return ans
    #
    # def numTeams(self, rating: List[int]) -> int:
    #     memo = {}
    #     ans = 0
    #     for i in range(len(rating)):
    #         incr = self.dp(rating, memo, True, i, 1)
    #         desc = self.dp(rating, memo, False, i, 1)
    #         ans += incr + desc
    #     return ans

    # def numTeams(self, rating: List[int]) -> int:
    #     # brute force
    #     # complexity: time O(n^3), mem O(1)
    #     n = len(rating)
    #     ans = 0
    #     for i in range(n-2):
    #         for j in range(i, n-1):
    #             for k in range(j, n):
    #                 if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
    #                     ans += 1

    #     return ans
