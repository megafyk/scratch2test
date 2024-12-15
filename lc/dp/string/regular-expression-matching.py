class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dfs string
        # time O(len(s)*len(p)), space O(len(s)*len(p))
        @cache
        def dfs(i,j):
            if i >= len(s) and j >= len(p): return True
            if j >= len(p): return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j+1 < len(p) and p[j+1] == "*":
                not_use_asterisk = dfs(i, j+2)
                use_asterisk = match and dfs(i+1, j)
                return not_use_asterisk or use_asterisk
            if match:
                return dfs(i+1, j+1)
            return False

        return dfs(0,0)
