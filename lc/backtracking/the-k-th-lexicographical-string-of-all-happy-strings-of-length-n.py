class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # binary tree
        # time O(n), space O(n)
        if k > 3 * (1 << (n-1)):
            return ""
        res = []
        prev = ""
        for i in range(n):
            for c in "abc":
                if c != prev:
                    if k > 1 << (n-i-1):
                        k -= 1 << (n-i-1)
                    else:
                        res.append(c)
                        prev = c
                        break
        return ''.join(res)

class Solution1:
    def getHappyString(self, n: int, k: int) -> str:
        q = deque()
        q.append("")
        h = 0
        while q:
            h += 1
            cnt = 0
            for i in range(len(q)):
                s = q.popleft()
                if n == h:
                    for c in "abc":
                        if len(s) == 0 or s[-1] != c:
                            cnt += 1
                            if cnt == k:
                                return s + c
                else:
                    for c in "abc":
                        if len(s) == 0 or s[-1] != c:
                            q.append(s + c)
        return ""


class Solution2:
    def getHappyString(self, n: int, k: int) -> str:
        # time O(n*2^n), space O(n)
        chars = ["a", "b", "c"]

        self.cnt = 0
        self.res = ""

        def backtrack(cur: str):
            if len(cur) == n:
                self.cnt += 1
                if self.cnt == k:
                    self.res = cur
                return
            for c in chars:
                if cur and cur[-1] == c:
                    continue
                backtrack(cur + c)
                if self.res:
                    return

        backtrack("")
        return self.res
