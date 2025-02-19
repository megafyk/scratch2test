class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # stack
        # time O(n), space O(n)
        res, st = [], []
        n = len(pattern)
        for i in range(n+1):
            st.append(i+1)
            while st and (i == n or pattern[i] == "I"):
                res.append(str(st.pop()))

        return ''.join(res)

        # # backtrack
        # # time O(9!), space O(n)
        # used = [False for _ in range(0, 10)]
        # n = len(pattern)
        # def backtrack(idx, num):
        #     if idx == n + 1: return num
        #     res = ""

        #     if pattern[idx-1] == "I":
        #         for i in range(1, 10):
        #             if used[i] or i < int(num[-1]): continue
        #             used[i] = True
        #             res = backtrack(idx+1, num+str(i))
        #             if len(res) == n+1:
        #                 return res
        #             used[i] = False
        #     else:
        #         for i in range(9, 0, -1):
        #             if used[i] or i > int(num[-1]): continue
        #             used[i] = True
        #             res = backtrack(idx+1, num+str(i))
        #             if len(res) == n+1:
        #                 return res
        #             used[i] = False
        #     return ""

        # for i in range(1,10):
        #     used[i] = True
        #     res = backtrack(1, str(i))
        #     used[i] = False
        #     if len(res) == n+1:
        #         return res
        # return ""