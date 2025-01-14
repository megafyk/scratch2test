class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        sA = set()
        sB = set()
        res = [0] * n
        for i in range(n):
            sA.add(A[i])
            sB.add(B[i])
            if A[i] == B[i]:
                res[i] = res[max(i-1, 0)] + 1
            else:
                if A[i] in sB and B[i] in sA:
                    res[i] += res[max(i-1, 0)] + 2
                elif A[i] in sB:
                    res[i] += res[max(i-1, 0)] + 1
                elif B[i] in sA:
                    res[i] += res[max(i-1, 0)] + 1
                else:
                    res[i] += res[max(i-1, 0)]
        return res
