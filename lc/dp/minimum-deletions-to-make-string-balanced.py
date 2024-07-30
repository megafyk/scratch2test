from collections import deque


class Solution:
    def minimumDeletions(self, s: str) -> int:
        # dp
        # complexity: time O(n), mem O(1)
        n = len(s)
        dp1, dp2 = 0, 0
        count_b = 0

        for i in range(n):
            if s[i] == "b":
                count_b += 1
            else:
                dp2 = min(dp1 + 1, count_b)
            dp1 = dp2
        return dp2

    # def minimumDeletions(self, s: str) -> int:
    #     # stack
    #     # complexity: time O(n), mem O(n)
    #     st = deque()
    #     ans = 0
    #     for ch in s:
    #         if st and st[-1] == "b" and ch == "a":
    #             st.pop()
    #             ans += 1
    #         else:
    #             st.append(ch)
    #     return ans
