class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # backtrack
        # time O(3^k), space O(1)
        def backtrack(x, cur_sum):
            if cur_sum == n: return True
            if cur_sum > n: return False
            for i in range(x+1, 16):
                if backtrack(i, cur_sum + 3 ** i):
                    return True
            return False

        return backtrack(-1, 0)
