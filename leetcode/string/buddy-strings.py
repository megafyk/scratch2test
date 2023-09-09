class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or len(s) <= 1:
            return False
        count = 0
        if s == goal:
            return len(s) - len(set(s)) >= 1
        c = d = ""
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                if count == 1:
                    c = goal[i]
                    d = s[i]
                if count == 2 and (c != s[i] or d != goal[i]):
                    return False
        return count == 2


s = Solution()
print(s.buddyStrings("ab", "ba"))
print(s.buddyStrings("abcaa", "abcbb"))
print(s.buddyStrings("abc", "acd"))
print(s.buddyStrings("abab", "abab"))
