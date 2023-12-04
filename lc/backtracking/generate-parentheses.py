from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        ans = set()
        gen_p = self.generateParenthesis(n - 1)

        for p in gen_p:
            open_idx = 0
            close_idx = open_idx + 1

            while open_idx < len(p) + 1:
                new_p = p[:open_idx] + "(" + p[open_idx:close_idx] + ")" + p[close_idx:]
                if new_p not in ans:
                    ans.add(new_p)
                if close_idx == len(p) + 1:
                    open_idx += 1
                    close_idx = open_idx
                close_idx += 1
        return list(ans)


s = Solution()
print(s.generateParenthesis(3))
