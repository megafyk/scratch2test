class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # combinatoric contraction
        # time O(1), space O(1)
        def calc(x):
            if x <= 0: return 0
            return x*(x-1) // 2
        return calc(n+2) - 3*calc(n-limit+1) + 3 * calc(n-2*(limit+1) + 2) - calc(n-3*(limit+1) + 2)