class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # complexity: time O(1), mem O(1)
        res = 0
        if start != goal:
            for i in range(33):
                bit_start = ((start >> i) & 1 == 1)
                bit_goal = ((goal >> i) & 1 == 1)
                if bit_start != bit_goal: res += 1
        return res
