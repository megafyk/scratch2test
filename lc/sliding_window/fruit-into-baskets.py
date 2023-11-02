from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        slow, fast = 0, 0
        d_win = {}
        ans = 0
        while fast < len(fruits):
            if fruits[fast] not in d_win:
                d_win[fruits[fast]] = 0
            d_win[fruits[fast]] += 1
            fast += 1
            while len(d_win) > 2:
                d_win[fruits[slow]] -= 1
                if d_win[fruits[slow]] == 0:
                    d_win.pop(fruits[slow])
                slow += 1

            ans = max(ans, fast - slow)

        return ans

s = Solution()
print(s.totalFruit([1,2,1]))
print(s.totalFruit([0,1,2,2]))
print(s.totalFruit([1,2,3,2,2]))
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
