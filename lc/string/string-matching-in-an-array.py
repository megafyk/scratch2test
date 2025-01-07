class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        for i in range(n):
            for j in range(n):
                if i != j and len(words[i]) < len(words[j]) and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res


    # def stringMatching(self, words: List[str]) -> List[str]:
    #     def check(w1, w2, pi):
    #         n = len(w1)
    #         j = 0

    #         for i in range(len(w2)):
    #             while j > 0 and w1[j] != w2[i]:
    #                 j = pi[j-1]
    #             if w1[j] == w2[i]:
    #                 j += 1
    #             if j == n:
    #                 return True
    #         return False

    #     res = []
    #     n = len(words)
    #     pis = []

    #     for w in words:
    #         pi = [0] * len(w)
    #         j = 0
    #         for i in range(1, len(w)):
    #             while j > 0 and w[j] != w[i]:
    #                 j = pi[j-1]
    #             if w[j] == w[i]:
    #                 j+=1
    #                 pi[i] = j
    #         pis.append(pi)

    #     res = []

    #     for i in range(n):
    #         for j in range(n):
    #             if i == j or len(words[i]) > len(words[j]):
    #                 continue
    #             if check(words[i], words[j], pis[i]):
    #                 res.append(words[i])
    #                 break 

    #     return res