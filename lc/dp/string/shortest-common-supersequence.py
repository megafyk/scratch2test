class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # dp string
        # time O(m*n), space O(m*n)
        m,n = len(str1), len(str2)
        prev = [str2[j:] for j in range(n)]
        prev.append("")
        for i in range(m-1, -1, -1):
            cur = [""] * n
            cur.append(str1[i:])
            for j in range(n-1, -1, -1):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prev[j+1]
                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + cur[j+1]
                    cur[j] = res1 if len(res1) < len(res2) else res2
            prev = cur
        return cur[0]

    # def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    #     @cache
    #     def dp(i,j):
    #         if i == len(str1):
    #             return str2[j:]
    #         if j == len(str2):
    #             return str1[i:]
    #         if str1[i] == str2[j]:
    #             return str1[i] + dp(i+1,j+1)
    #         else:
    #             res1 = str1[i] + dp(i+1,j)
    #             res2 = str2[j] + dp(i,j+1)
    #             if len(res1) < len(res2):
    #                 return res1
    #             return res2
    #     return dp(0,0)