class Solution:
    def maxDepth(self, s: str) -> int:
        count = t = 0
        for c in s:
            if c == "(":
                t += 1
                count = max(count, t)
            elif c == ")":
                t -= 1
        return count

s = Solution()
print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
