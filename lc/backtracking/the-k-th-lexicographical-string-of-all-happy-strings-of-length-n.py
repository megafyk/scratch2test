class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # array partition size
        # time O(n), space O(n)
        total_happy = 3*(2**(n-1))
        l,r = 1, total_happy
        res = []
        choices = "abc"
        for i in range(n):
            cur = l
            partition_size = (r-l + 1) // (len(choices))
            for c in choices:
                if cur <= k < cur+partition_size:
                    res.append(c)
                    l = cur
                    r = cur + partition_size - 1
                    choices = "abc".replace(c, "")
                    break
                cur += partition_size
            
        return ''.join(res)
    # def getHappyString(self, n: int, k: int) -> str:
    #     # time O(n*2^n), space O(n)
    #     chars = ['a', 'b', 'c']

    #     self.cnt = 0
    #     self.res = ""
    #     def backtrack(cur: str):
    #         if len(cur) == n:
    #             self.cnt += 1
    #             if self.cnt == k:
    #                 self.res = cur
    #             return
    #         for c in chars:
    #             if cur and cur[-1] == c:
    #                 continue
    #             backtrack(cur + c)
    #             if self.res:
    #                 return
    #     backtrack("")
    #     return self.res
